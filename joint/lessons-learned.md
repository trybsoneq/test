---
schema: cybersparring/v0.1
type: lessons_learned
team: joint
id: LESSONS-001
session_id: CS-XXXX
phase: review
---
# Lessons Learned — wnioski na podstawie planu

## Najważniejsze odkrycia obu osób
Plan wymaga skoordynowania zapory, usług systemowych, ustawień Apache, ochrony plików i AppArmor. Rzetelny przegląd wymaga oddzielnego zapisu obserwacji, interpretacji i dowodu.

## Czego nauczyła się Blue?
Samo wdrożenie ustawień nie dowodzi skuteczności. Należy sprawdzić porty, konfigurację Apache, metody HTTP, prawa plików, atrybuty i tryb AppArmor. Reguły zapory muszą uwzględniać wymagane kanały administracyjne.

## Czego nauczyła się Red?
Plan testów trzeba ograniczyć do jasno wskazanego, autoryzowanego celu. Hipotezy o portach, nagłówkach i zasobach nie są ustaleniami do czasu zebrania powtarzalnego dowodu.

## Co zmienimy w następnej rundzie?
Przed startem zapisać IP celu, system i wersje, zakres/okno testów oraz stan początkowy. Po każdej fazie zachować zanonimizowane wyniki poleceń i dokładny czas.

## Czy szablon raportu z pentestu był przydatny?
Struktura ID dla hardeningu, testów, kroków i ustaleń ułatwia śledzenie zależności. Należy konsekwentnie odróżniać rekord zaplanowany od wykonanego i zweryfikowanego.

## Uwagi o współpracy
Wspólny przegląd powinien odbyć się po zamrożeniu konfiguracji BLUE i zakończeniu RED. Nie uzupełniać retrospektywnie hipotez ani nie dopisywać niezaobserwowanych wyników.
