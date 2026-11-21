# ![INFO](assets/icons/info.svg) CyberSparring — szablon ćwiczenia v0.1.6

> **Status: PROTOTYP** · Markdown + YAML · Bez wtyczek Obsidiana

# Praca lokalna w Obsidianie
Jeśli pracujesz na lokalnej kopii szablonu, w Obsidianie może być wygodniej. Otwierasz cały folder ćwiczenia i masz w jednym miejscu drzewo plików, edytor Markdown oraz podgląd notatek. Dzięki temu łatwo przechodzisz między instrukcją, dokumentacją swojej roli i plikami do wspólnego przeglądu.

Aby zacząć, pobierz z repozytorium CyberSparring_Obsidian.zip, rozpakuj go i otwórz folder CyberSparring jako skarbiec (Open folder as vault). Obsidian jest opcjonalny. Możesz też użyć dowolnego edytora Markdown.

## Legenda (FROZEN)

| ![RED](assets/icons/red.svg) RED | ![BLUE](assets/icons/blue.svg) BLUE | ![JOINT](assets/icons/joint.svg) JOINT | ![INFO](assets/icons/info.svg) INFO |
|---|---|---|---|
| Testy penetracyjne | Konfiguracja i hardening | Wspólny przegląd | Instrukcje |

## Pobierzcie szablon

Otwórzcie [repozytorium CyberSparring](https://github.com/cybersparing/cybersparring-template). Wybierzcie sposób pracy podany w zadaniu Moodle.

- **GitHub.** Wybierzcie **Use this template → Create a new repository**. RED i BLUE tworzą osobne repozytoria z widocznością **Private**. Sklonujcie własne repozytoria, jeśli chcecie edytować pliki lokalnie lub używać Obsidiana.
- **Lokalnie w Obsidianie.** W repozytorium otwórzcie [`CyberSparring_Obsidian.zip`](https://github.com/cybersparing/cybersparring-template/blob/main/CyberSparring_Obsidian.zip) i kliknijcie przycisk pobierania pliku. Rozpakujcie ZIP. W Obsidianie wybierzcie **Otwórz folder jako skarbiec** (*Open folder as vault*) i wskażcie folder `CyberSparring`, w którym znajduje się `session.yaml`. RED i BLUE pracują w osobnych kopiach folderu. Tę samą paczkę można edytować w dowolnym edytorze Markdown.

## Uzupełnijcie dane ćwiczenia

1. Weźcie numer edycji i temat z Moodle. Połączcie numer edycji z numerem swojej sekcji, np. `CS-01-S02` oznacza CyberSparring 1, sekcja 2.
2. W obu kopiach zamieńcie `CS-XXXX` na swój CS-ID w `session.yaml`, w nagłówkach YAML dokumentów z polem `session_id` oraz w `common/rules.md`. Możecie użyć funkcji **Zamień w plikach** w edytorze. W `session.yaml` wpiszcie temat w polu `scenario`. Używajcie tego samego CS-ID w kolejnych dokumentach.
3. **![BLUE](assets/icons/blue.svg) BLUE** dokumentuje pracę w `blue/` i `joint/hardening-observations-blue.md`. **![RED](assets/icons/red.svg) RED** dokumentuje pracę w `red/` i `joint/pentest-preparation-notes-red.md`. W trybie **black box** dokumentację BLUE udostępnijcie RED podczas wspólnego przeglądu.

## Wspólny przegląd i oddanie

1. **![JOINT](assets/icons/joint.svg) JOINT.** Po testach skopiujcie do jednej wspólnej kopii katalogi `blue/` i `red/` oraz obie notatki z `joint/`. Uzupełnijcie `joint/joint-review.md` i `joint/lessons-learned.md`. Ich treść utworzy raport PDF. Naprawy i retesty dopiszcie jako nowe rekordy.
2. W głównym katalogu wspólnej kopii zapiszcie kopię `sklad-sekcji.example.yaml` jako `sklad-sekcji.yaml`. Wpiszcie imiona i nazwiska w listach odpowiednich ról, po jednej osobie na wiersz. Przy kilku osobach dodajcie kolejne wiersze z myślnikiem.

   ```yaml
   red:
     - Imię i nazwisko
   blue:
     - Imię i nazwisko
   ```

3. W katalogu głównym wspólnej kopii zainstalujcie zależności i wygenerujcie oba pliki.

   ```bash
   python -m pip install -r requirements.txt
   python scripts/validate.py --submit
   ```

   Jeśli polecenie `python` jest niedostępne, użyjcie `py -3` w Windows lub `python3` w Linuksie.
4. Poprawcie komunikaty **BŁĄD** i sprawdźcie komunikaty **UWAGA**. Po udanej walidacji skrypt zapisze PDF i ZIP **obok katalogu** wspólnej kopii. Otwórzcie PDF i sprawdźcie jego treść oraz skład sekcji. Skład z pliku `sklad-sekcji.yaml` trafia do PDF. Ten plik YAML pozostaje lokalny.
5. Jedna osoba z sekcji przesyła oba pliki w zadaniu Moodle, np. `CS-01-S02.pdf` i `CS-01-S02.zip`.

## Zasady danych i bezpieczeństwa

- Testuj wyłącznie wskazane, izolowane środowisko, w uzgodnionym oknie czasowym; zakres autoryzacji wpisz w `common/rules.md`.
- **Nie zapisuj** haseł, tokenów, kluczy prywatnych, danych osobowych, prawdziwych danych z produkcji ani exploitów ukierunkowanych na cudze systemy. Przed dołączeniem wyników usuń sekrety i identyfikatory wrażliwe.
- **Nie commituj** obrazów maszyn, dużych dumpów, `.env`, kluczy i logów zawierających dane wrażliwe; patrz `.gitignore`.
- Notuj także testy bez ustaleń, błędne hipotezy i nieudane próby. Odróżniaj **obserwację** od **interpretacji**.
- W YAML uzupełniaj pola bez zmiany ich nazw. Nagłówki Markdown możesz rozwijać. W identyfikatorach używaj `HARD-001`, `TEST-001`, `STEP-001`, `FIND-001` itd. bez powtórzeń wewnątrz sesji.
