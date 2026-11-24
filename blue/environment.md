---
schema: cybersparring/v0.1
type: environment
team: blue
id: ENV-001
session_id: CS-01-S06
target_id: SRV-001
status: completed
---
# Środowisko i punkt wyjścia

## System, usługi i cel
Plan zakłada minimalną instalację jednej z dystrybucji:
- Debian 12 (Bookworm) Netinst, albo
- Ubuntu Server 24.04 LTS Minimal.

Docelową usługą jest Apache HTTP Server. Przewidziano UFW, ModSecurity (WAF), mod_evasive oraz AppArmor. Użytkownik potwierdził wykonanie prac po stronie BLUE. Nie przekazano jednak informacji o faktycznie użytej dystrybucji ani wersjach pakietów.

## Początkowy stan i powierzchnia ataku
Nie przekazano pomiarów stanu początkowego. W raporcie należy uzupełnić je z notatek, jeśli zostały zachowane:
- system i wersje: `cat /etc/os-release`, `apache2 -v`;
- usługi i porty: `sudo ss -tulpn`;
- aktywne usługi: `systemctl --type=service --state=running`;
- konfiguracja Apache: `sudo apache2ctl -S`, `sudo apache2ctl -M`.

Adres IP i wyniki poleceń pozostają nieudokumentowane w dostarczonych materiałach.

## Ograniczenia i założenia
- Środowisko musi być odizolowane i jednoznacznie wskazane w `common/rules.md`.
- Zakładany czas BLUE: 60 minut; RED: 120 minut.
- Plan wymienia SSH, HTTP/HTTPS, UFW, Apache, ModSecurity, mod_evasive i AppArmor.
- Należy zweryfikować, czy profil AppArmor dla Apache istnieje i czy może być bezpiecznie włączony w trybie enforce.
- Zanim wyłączysz SSH, potwierdź, że nie jest wymagane do administracji/oceny; wyłącz dostęp alternatywną konsolą VM, aby nie utracić zarządzania.
