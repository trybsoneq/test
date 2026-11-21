---
schema: cybersparring/v0.1
type: reflection
team: blue
id: REF-BLUE-001
session_id: CS-XXXX
phase: preparation
---
# Blue — obserwacje z planowania hardeningu

## Co było trudne?
Na podstawie planu widać, że trzeba skoordynować kilka warstw: usługę SSH, zaporę UFW, moduły Apache, prawa do katalogu WWW i AppArmor. Największą kwestią operacyjną jest takie ustawienie UFW i SSH, aby nie utracić wymaganego dostępu administracyjnego.

## Co uznałem/am za wystarczająco zabezpieczone — i dlaczego?
Plan przewiduje ograniczenie ruchu przychodzącego, wyłączenie zbędnych modułów, ograniczenie metod HTTP, ukrycie wersji serwera i ochronę plików WWW przed zapisem procesu serwera. Nie ma jeszcze pomiarów, które pozwalałyby uznać zabezpieczenia za skuteczne.

## Czego nie zdążyłem/am lub nie potrafiłem/am sprawdzić?
Nie dostarczono informacji o instalacji, konfiguracji, statusie usług, regułach UFW, aktywnym profilu AppArmor ani wynikach testów HTTP. Nie można ustalić, które kroki rzeczywiście wykonano.

## Wątpliwości i hipotezy przed poznaniem wyników Red
- Czy wyłączenie SSH jest zgodne z zasadami laboratorium i czy pozostał dostęp konsolowy?
- Czy konfiguracja Apache przechodzi `apache2ctl configtest`?
- Czy UFW dopuszcza wszystkie wymagane porty, a blokuje pozostałe?
- Czy AppArmor posiada właściwy profil w trybie enforce?
- Czy atrybut immutable nie blokuje planowanego procesu aktualizacji strony?

> Notatka oparta na planie PDF; nie jest relacją z wykonanych prac.
