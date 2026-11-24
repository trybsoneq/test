---
schema: cybersparring/v0.1
type: reflection
team: blue
id: REF-BLUE-001
session_id: CS-01-S06
phase: preparation
---
# Blue — obserwacje z planowania hardeningu

## Co było trudne?
Prace BLUE zostały wykonane przez użytkownika, który pełnił również rolę RED. Ważnym problemem organizacyjnym było nieprzygotowanie serwera docelowego przez drugą stronę, co zablokowało testy RED.

## Co uznałem/am za wystarczająco zabezpieczone — i dlaczego?
Plan przewiduje ograniczenie ruchu przychodzącego, wyłączenie zbędnych modułów, ograniczenie metod HTTP, ukrycie wersji serwera i ochronę plików WWW przed zapisem procesu serwera. Nie ma jeszcze pomiarów, które pozwalałyby uznać zabezpieczenia za skuteczne.

## Czego nie zdążyłem/am lub nie potrafiłem/am sprawdzić?
Nie przekazano szczegółowych logów konfiguracji ani wyników poleceń, dlatego nie można niezależnie potwierdzić każdej zmiany. Serwer docelowy dla RED nie został przygotowany.

## Wątpliwości i hipotezy przed poznaniem wyników Red
- Czy wyłączenie SSH jest zgodne z zasadami laboratorium i czy pozostał dostęp konsolowy?
- Czy konfiguracja Apache przechodzi `apache2ctl configtest`?
- Czy UFW dopuszcza wszystkie wymagane porty, a blokuje pozostałe?
- Czy AppArmor posiada właściwy profil w trybie enforce?
- Czy atrybut immutable nie blokuje planowanego procesu aktualizacji strony?

> Notatka oparta na planie PDF; nie jest relacją z wykonanych prac.
