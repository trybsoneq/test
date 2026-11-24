---
schema: cybersparring/v0.1
type: test_case
team: red
id: TEST-001
session_id: CS-01-S06
target_id: SRV-001
objective: "Ocena ekspozycji usług i podstawowego hardeningu Apache w autoryzowanej VM"
status: planned
expected: "Widoczne są wyłącznie uzgodnione usługi; konfiguracja HTTP nie ujawnia zbędnych informacji i odrzuca niedozwolone metody"
actual: "Brak wyników pomiarów w dostarczonym PDF — zawiera on scenariusz, nie log wykonania"
related_finding_ids: []
---
# TEST-001 — Weryfikacja ekspozycji i konfiguracji WWW

## Warunki wstępne
- Pisemnie/wyraźnie zatwierdzony zakres w `common/rules.md`, wskazany adres własnej docelowej VM i okno testowe.
- Etap BLUE zakończony, konfiguracja zamrożona.
- RED pracuje wyłącznie z własnej VM Kali w izolowanej sieci laboratoryjnej.

## Plan sprawdzenia
1. Ustalić adres docelowej VM z konfiguracji laboratorium lub od prowadzącego; nie skanować obcej sieci.
2. Wykonać ograniczony rekonesans usług w zatwierdzonym zakresie, początkowo tylko portów przewidzianych dla usługi.
3. Dla HTTP sprawdzić stronę, nagłówki odpowiedzi, metody OPTIONS/HEAD oraz widoczność katalogów.
4. Sprawdzić zasoby WWW metodą enumeracji o niskim wpływie i z ograniczonym zakresem.
5. Udokumentować odpowiedzi, czas, parametry i ograniczenia bez danych uwierzytelniających.

## Kryterium powodzenia / niepowodzenia
Sukces kontroli hardeningu: ekspozycja zgodna z uzgodnioną listą usług, brak ujawniania wersji Apache/OS, brak listowania katalogów oraz odrzucenie metod innych niż uzgodnione. Każde odstępstwo wymaga odrębnego, potwierdzonego dowodu i oceny wpływu.

## Wynik i ograniczenia
Status: zaplanowany, nieuruchomiony według dostarczonych materiałów. Nie ma rzeczywistych wyników ani dowodów, więc nie można potwierdzić podatności ani skuteczności zabezpieczeń.

Nie wykonywać testów słownikowych Hydra, LFI, Command Injection, Shellshock, eskalacji uprawnień ani prób zapisu/modyfikacji strony bez odrębnej zgody prowadzącego i przeznaczonego do tego odtwarzalnego celu testowego.
