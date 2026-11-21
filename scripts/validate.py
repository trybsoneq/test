#!/usr/bin/env python3
"""CyberSparring v0.1 — local validation (and optional packaging)."""
import argparse
import re
import sys
import zipfile
from tempfile import TemporaryDirectory
from pathlib import Path
try:
    import yaml
except ImportError:
    print("Brak PyYAML. Uruchom: python -m pip install -r requirements.txt")
    sys.exit(2)

ROOT = Path(__file__).resolve().parents[1]
DOCS = {
    "blue/environment.md": ("environment", "blue"),
    "blue/hardening/HARD-001.md": ("hardening", "blue"),
    "red/test-cases/TEST-001.md": ("test_case", "red"),
    "red/pentest-log/STEP-001.md": ("test_step", "red"),
    "red/findings/FIND-001.md": ("finding", "red"),
    "joint/hardening-observations-blue.md": ("reflection", "blue"),
    "joint/pentest-preparation-notes-red.md": ("reflection", "red"),
    "joint/joint-review.md": ("joint_review", "joint"),
    "joint/lessons-learned.md": ("lessons_learned", "joint"),
    "joint/remediation/REMED-001.md": ("remediation", "joint"),
}
VALID_TYPES = {x[0] for x in DOCS.values()} | {"rules"}
ID_PATTERN = re.compile(r"^[A-Z][A-Z0-9-]*-\d{3}$")
REQUIRED = {"schema", "type", "team", "id", "session_id"}
REF_FIELDS = {"test_case_id", "related_test_ids", "related_step_ids", "related_finding_ids", "related_hardening_ids"}
PLACEHOLDERS = ("[uzupełnij]", "[opis]", "[cel", "[co ", "[system", "[metoda", "[wynik", "[fakt", "[ścieżki", "[krótki", "[spodziewany", "[rzeczywisty")
SKIP_PARTS = {".git", ".obsidian", ".trash", "__pycache__", "sklad-sekcji.yaml", "sklad-sekcji.example.yaml"}
CS_ID_PATTERN = re.compile(r"CS-(0[1-9]|[1-9][0-9])-S(0[1-9]|[1-9][0-9])")

def read_frontmatter(path):
    body = path.read_text(encoding="utf-8")
    m = re.match(r"\A---\s*\n(.*?)\n---\s*\n", body, re.S)
    if not m:
        raise ValueError("brak YAML frontmatter")
    data = yaml.safe_load(m.group(1))
    if not isinstance(data, dict):
        raise ValueError("frontmatter nie jest mapą YAML")
    return data, body[m.end():]

def pack_archive(archive):
    with zipfile.ZipFile(archive, "w", zipfile.ZIP_DEFLATED) as z:
        for p in sorted(ROOT.rglob("*")):
            if p.is_symlink() or not p.is_file() or any(part in SKIP_PARTS for part in p.relative_to(ROOT).parts):
                continue
            if p.suffix.lower() in (".key", ".pem", ".p12", ".pfx", ".kdbx", ".pcap", ".pcapng", ".dump", ".zip", ".vmdk", ".vdi", ".qcow2", ".ova") or p.name.startswith(".env"):
                continue
            z.write(p, arcname=f"{ROOT.name}/{p.relative_to(ROOT).as_posix()}")


def main():
    parser = argparse.ArgumentParser(description="Sprawdź sesję CyberSparring przed oddaniem")
    output = parser.add_mutually_exclusive_group()
    output.add_argument("--submit", action="store_true", help="Po poprawnej walidacji stwórz PDF i ZIP")
    output.add_argument("--pack", action="store_true", help="Po poprawnej walidacji stwórz ZIP")
    args = parser.parse_args()
    errors, warnings = [], []
    try:
        session = yaml.safe_load((ROOT / "session.yaml").read_text(encoding="utf-8"))
    except Exception as exc:
        print(f"BŁĄD session.yaml: {exc}")
        return 1
    if not isinstance(session, dict):
        errors.append("session.yaml musi być mapą YAML")
        session = {}
    sid = session.get("session_id")
    if not isinstance(sid, str) or not re.fullmatch(r"CS-[A-Z0-9]+(?:-[A-Z0-9]+)*", sid) or sid == "CS-XXXX":
        errors.append("session.yaml: wpisz CS-ID w polu session_id (np. CS-01-S02)")
    event_section = CS_ID_PATTERN.fullmatch(sid) if isinstance(sid, str) else None
    if args.submit and event_section is None:
        errors.append("session.yaml: do oddania wpisz CS-ID w formacie CS-NN-SMM (np. CS-01-S02)")
    topic = session.get("scenario")
    if args.submit and (not isinstance(topic, str) or not topic.strip() or topic.strip().startswith("[")):
        errors.append("session.yaml: wpisz temat ćwiczenia w polu scenario")
    for k in ("team_id", "red_id", "blue_id", "started_at", "review_at"):
        val = str(session.get(k, ""))
        if not val or "XX" in val or "YYYY" in val:
            warnings.append(f"session.yaml: nieuzupełnione pole {k}")
    ids, links = {}, []
    for rel in DOCS:
        if not (ROOT / rel).exists():
            errors.append(f"brak pliku {rel}")
    # Also read copied/additional Markdown files (for multiple tests/findings).
    for p in sorted(ROOT.rglob("*.md")):
        if any(part in SKIP_PARTS for part in p.relative_to(ROOT).parts):
            continue
        rel = p.relative_to(ROOT).as_posix()
        if rel == "README.md" or rel.endswith("/README.md"):
            continue
        try:
            data, body = read_frontmatter(p)
        except Exception as exc:
            errors.append(f"{rel}: {exc}")
            continue
        if data.get("schema") != "cybersparring/v0.1":
            errors.append(f"{rel}: niepoprawny schema")
        if data.get("type") not in VALID_TYPES:
            errors.append(f"{rel}: nieznany type")
        if data.get("type") == "rules":
            continue
        missing = [k for k in REQUIRED if k not in data or data[k] in (None, "")]
        if missing:
            errors.append(f"{rel}: brak pól {', '.join(missing)}")
        expected_team = "blue" if rel.startswith("blue/") else "red" if rel.startswith("red/") else None
        if expected_team and data.get("team") != expected_team:
            errors.append(f"{rel}: team powinien wynosić {expected_team}")
        if data.get("session_id") != sid:
            errors.append(f"{rel}: session_id różni się od session.yaml")
        doc_id = data.get("id")
        if not isinstance(doc_id, str) or not ID_PATTERN.fullmatch(doc_id):
            errors.append(f"{rel}: niepoprawny id: {doc_id}")
        elif doc_id in ids:
            errors.append(f"{rel}: powtórzony identyfikator {doc_id} ({ids[doc_id]})")
        else:
            ids[doc_id] = rel
        for field in REF_FIELDS:
            val = data.get(field)
            if val is None:
                continue
            refs = val if isinstance(val, list) else [val]
            if not all(isinstance(x, str) for x in refs):
                errors.append(f"{rel}: {field} musi zawierać ID / listę ID")
            else:
                links.extend((rel, field, x) for x in refs)
        for evidence in data.get("evidence_paths", []) or []:
            if not isinstance(evidence, str):
                errors.append(f"{rel}: evidence_paths musi zawierać ścieżki tekstowe")
                continue
            resolved = (p.parent / evidence).resolve()
            if not resolved.is_relative_to(ROOT.resolve()):
                errors.append(f"{rel}: evidence_paths wychodzi poza katalog sesji")
            elif not resolved.is_file():
                errors.append(f"{rel}: brak dowodu: {evidence}")
        if any(placeholder in body.lower() for placeholder in PLACEHOLDERS):
            warnings.append(f"{rel}: prawdopodobnie pozostały instrukcje w nawiasach []")
        if str(data.get("status", "")) == "planned":
            warnings.append(f"{rel}: status nadal planned")
        if data.get("type") == "finding" and not data.get("evidence_paths"):
            warnings.append(f"{rel}: finding bez dowodów (evidence_paths)")
    for rel, field, ident in links:
        if ident not in ids:
            errors.append(f"{rel}: {field} wskazuje brakujący ID {ident}")
    print(f"Dokumenty z ID: {len(ids)} | Błędy: {len(errors)} | Ostrzeżenia: {len(warnings)}")
    for msg in errors:
        print("BŁĄD:", msg)
    for msg in warnings:
        print("UWAGA:", msg)
    if errors:
        print("WALIDACJA NIEUDANA — popraw błędy przed pakowaniem.")
        return 1
    if args.submit:
        from submission import render_report
        try:
            with TemporaryDirectory(dir=ROOT.parent) as tmp:
                staging = Path(tmp)
                pdf = staging / f"{sid}.pdf"
                archive = staging / f"{sid}.zip"
                render_report(ROOT, session, event_section, pdf, read_frontmatter)
                pack_archive(archive)
                pdf.replace(ROOT.parent / pdf.name)
                archive.replace(ROOT.parent / archive.name)
        except Exception as exc:
            print(f"BŁĄD przygotowania plików: {exc}")
            return 1
        print("PDF:", ROOT.parent / pdf.name)
        print("ZIP:", ROOT.parent / archive.name)
    if args.pack:
        archive = ROOT.parent / f"{sid}.zip"
        pack_archive(archive)
        print("ZIP:", archive)
    print("Walidacja struktury OK. Ostrzeżenia sprawdź ręcznie; parser nie potwierdza poprawności merytorycznej.")
    return 0
if __name__ == "__main__":
    sys.exit(main())
