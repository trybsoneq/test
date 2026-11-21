"""Render the joint Markdown report and its cover as a PDF."""
from html import escape
from pathlib import Path
from urllib.parse import unquote, urlsplit

import yaml


def load_roster(path):
    if not path.is_file():
        raise ValueError("Skopiuj skład sekcji z pliku sklad-sekcji.example.yaml do sklad-sekcji.yaml i uzupełnij oba pola.")
    roster = yaml.safe_load(path.read_text(encoding="utf-8"))
    for role in ("red", "blue"):
        names = roster.get(role) if isinstance(roster, dict) else None
        if not isinstance(names, list) or not names or any(
            not isinstance(name, str) or not name.strip() for name in names
        ):
            raise ValueError(f"sklad-sekcji.yaml: wpisz skład roli {role.upper()} jako listę nazwisk.")
    return roster


def render_report(root, session, event_section, output, read_frontmatter):
    from markdown_it import MarkdownIt
    from xhtml2pdf import pisa

    roster = load_roster(root / "sklad-sekcji.yaml")
    event, section = map(int, event_section.groups())
    cs_id = escape(session["session_id"])
    topic = escape(session["scenario"])
    red = escape(", ".join(roster["red"]))
    blue = escape(", ".join(roster["blue"]))
    markdown = MarkdownIt("commonmark", {"html": False}).enable("table")
    joint = root / "joint"
    reports = ("joint-review.md", "lessons-learned.md")
    body = "".join(
        markdown.render(read_frontmatter(joint / name)[1])
        for name in reports
    )

    document = f"""<!doctype html>
<html lang="pl">
<meta charset="utf-8">
<title>{cs_id} – CyberSparring</title>

<style>
@page {{ size: A4; margin: 18mm 19mm; }}
@font-face {{ font-family: Report; src: url("DejaVuSans.ttf"); }}
@font-face {{ font-family: Report; src: url("DejaVuSans-Bold.ttf"); font-weight: bold; }}
@font-face {{ font-family: Report; src: url("DejaVuSans-Oblique.ttf"); font-style: italic; }}
@font-face {{ font-family: Report; src: url("DejaVuSans-BoldOblique.ttf"); font-weight: bold; font-style: italic; }}
body {{ font-family: Report; font-size: 10pt; line-height: 1.4; color: #202829; }}
header {{ border-top: 4px solid #236454; padding-top: 16px; margin-bottom: 24px; }}
header h1 {{ margin: 6px 0; font-size: 24pt; }}
header p {{ margin: 4px 0; }}
main h1 {{ font-size: 17pt; border-bottom: 1px solid #a6b8b1; }}
main h2 {{ font-size: 13pt; }}
h1, h2, h3 {{ -pdf-keep-with-next: true; }}
pre {{ white-space: pre-wrap; overflow-wrap: anywhere; padding: 8px; background: #edf2ef; }}
img {{ max-width: 100%; max-height: 200mm; }}
th, td {{ padding: 4px 8px; border: 1px solid #a6b8b1; text-align: left; }}
</style>
<header>
<p>{cs_id} · Sekcja {section}</p>
<h1>CyberSparring {event}</h1>
<p><strong>{topic}</strong></p>
<p><strong>RED</strong> · {red}</p>
<p><strong>BLUE</strong> · {blue}</p>
</header>
<main>{body}</main>
"""
    fonts = Path(__file__).resolve().parent / "fonts"

    def local_resource(uri, _base):
        if uri in {"DejaVuSans.ttf", "DejaVuSans-Bold.ttf", "DejaVuSans-Oblique.ttf", "DejaVuSans-BoldOblique.ttf"}:
            return str(fonts / uri)
        parsed = urlsplit(uri)
        if parsed.scheme or parsed.netloc:
            raise ValueError(f"Obraz w raporcie musi wskazywać plik lokalny: {uri}")
        image = (joint / unquote(parsed.path)).resolve()
        if not image.is_relative_to(root) or not image.is_file():
            raise ValueError(f"Brak obrazu w dokumentacji: {uri}")
        return str(image)

    with output.open("wb") as pdf:
        result = pisa.CreatePDF(document, dest=pdf, link_callback=local_resource, encoding="utf-8")
    if result.err:
        raise ValueError("Nie udało się wyrenderować raportu PDF.")
