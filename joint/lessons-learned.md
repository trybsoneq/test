---
schema: cybersparring/v0.1
type: lessons_learned
team: joint
id: LESSONS-001
session_id: CS-01-S06
phase: review
---
# Lessons Learned — wnioski na podstawie planu

## Najważniejsze odkrycia obu osób
Użytkownik wykonał prace BLUE, ale etap RED został zablokowany, ponieważ druga strona nie przygotowała serwera docelowego. Ćwiczenie pokazuje, że dostępność celu i uzgodnienie odpowiedzialności są warunkami rozpoczęcia testów.

## Czego nauczyła się Blue?
Samo wdrożenie ustawień nie dowodzi skuteczności. Należy sprawdzić porty, konfigurację Apache, metody HTTP, prawa plików, atrybuty i tryb AppArmor. Reguły zapory muszą uwzględniać wymagane kanały administracyjne.

## Czego nauczyła się Red?
Przed rozpoczęciem RED należy sprawdzić, czy serwer docelowy faktycznie działa, jest osiągalny z Kali i został przekazany do testów. Bez tego nie można zebrać dowodów ani wyciągać wniosków o podatnościach.

## Co zmienimy w następnej rundzie?
Przed startem wyznaczyć osobę odpowiedzialną za przygotowanie serwera, potwierdzić jego dostępność z Kali i ustalić procedurę awaryjną, gdy środowisko nie będzie gotowe. Zapisać IP, system, wersje i wyniki poleceń.

## Czy szablon raportu z pentestu był przydatny?
Struktura ID dla hardeningu, testów, kroków i ustaleń ułatwia śledzenie zależności. Należy konsekwentnie odróżniać rekord zaplanowany od wykonanego i zweryfikowanego.

## Uwagi o współpracy
Wspólny przegląd powinien odbyć się po zamrożeniu konfiguracji BLUE i zakończeniu RED. Nie uzupełniać retrospektywnie hipotez ani nie dopisywać niezaobserwowanych wyników.
