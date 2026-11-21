---
schema: cybersparring/v0.1
type: rules
team: info
---
# Zakres i reguły sparingu

## Uzgodnienia przed startem
- **CS-ID:** CS-XXXX — do uzupełnienia zgodnie z Moodle
- **Cel / technologia:** utwardzanie serwera WWW Apache na Debian 12 (Bookworm) Netinst lub Ubuntu Server 24.04 LTS Minimal oraz kontrolowany przegląd z Kali Linux.
- **Autoryzowane środowisko (bez sekretów):** wyłącznie dedykowane, izolowane maszyny wirtualne serwera Apache i Kali Linux przygotowane na potrzeby laboratorium; konkretne adresy i sieć do wpisania przed testami.
- **Dozwolony zakres testów:** weryfikacja dostępności usług i portów, konfiguracji HTTP/Apache, metod HTTP, widocznych zasobów WWW oraz zabezpieczeń opisanych w scenariuszu; testy wyłącznie wobec wskazanego serwera i w uzgodnionym oknie.
- **Wyłączone działania / granice:** systemy osób trzecich i sieci poza laboratorium; destrukcyjne zmiany, trwałość, eksfiltracja, użycie znalezionych haseł/kluczy poza ćwiczeniem i testy obciążeniowe. Testy próbujące modyfikować stronę, logować się lub eskalować uprawnienia wyłącznie po wyraźnym zatwierdzeniu prowadzącego i w odtwarzalnym środowisku testowym.
- **BLUE — czas przygotowania i utwardzania środowiska:**
  - **Od (data i godzina):** do uzgodnienia
  - **Do (data i godzina):** do uzgodnienia (limit planu: 60 minut)
- **RED — czas przeprowadzania testów penetracyjnych:**
  - **Od (data i godzina):** do uzgodnienia
  - **Do (data i godzina):** do uzgodnienia (limit planu: 120 minut)
- **JOINT — termin wspólnego przeglądu wyników (data i godzina):** do uzgodnienia
- **Strefa czasowa:** `Europe/Warsaw`
- **Model wiedzy Red:** black box (zgodnie z `session.yaml`)

## Zasady operacyjne
- Przed rozpoczęciem potwierdzić adres docelowej VM, segment sieci, okno czasowe i zgodę prowadzącego.
- Po etapie BLUE zamrozić konfigurację na czas RED; naprawy dokumentować dopiero jako osobne rekordy JOINT.
- Nie kopiować historii terminala, kluczy SSH, haseł ani danych innych użytkowników. Weryfikację dostępu lokalnego prowadzić na własnych kontach/VM i bez odczytywania cudzych sekretów.
- Nie wykonywać testów Hydra, LFI, Command Injection, Shellshock, eskalacji uprawnień ani prób nadpisania strony bez wyraźnego zatwierdzenia i bezpiecznego celu testowego. Preferować walidację konfiguracji i nieinwazyjne testy kontrolne.
- Nie zapisywać sekretów, danych osobowych ani danych produkcyjnych w repozytorium.

> Plik dokumentuje proponowany zakres. Nie stanowi dowodu autoryzacji ani wykonania ćwiczenia; pola zespołu i terminów pozostają do potwierdzenia.
