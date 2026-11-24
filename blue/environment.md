---
schema: cybersparring/v0.1
type: environment
team: blue
id: ENV-001
session_id: CS-01-S06
target_id: SRV-001
status: planned
---
# Środowisko i punkt wyjścia

## System, usługi i cel
Plan zakłada minimalną instalację jednej z dystrybucji:
- Debian 12 (Bookworm) Netinst, albo
- Ubuntu Server 24.04 LTS Minimal.

Docelową usługą jest Apache HTTP Server. Przewidziano UFW, ModSecurity (WAF), mod_evasive oraz AppArmor. PDF nie potwierdza, którą dystrybucję faktycznie zainstalowano ani jakie wersje pakietów działają.

## Początkowy stan i powierzchnia ataku
Stan początkowy nie został udokumentowany pomiarami. Do zebrania na własnej VM przed hardeningiem:
- system i wersje: `cat /etc/os-release`, `apache2 -v`;
- usługi i porty: `sudo ss -tulpn`;
- aktywne usługi: `systemctl --type=service --state=running`;
- konfiguracja Apache: `sudo apache2ctl -S`, `sudo apache2ctl -M`.

Nie wpisano adresu IP ani wyników poleceń, ponieważ PDF zawiera plan, a nie log z maszyny.

## Ograniczenia i założenia
- Środowisko musi być odizolowane i jednoznacznie wskazane w `common/rules.md`.
- Zakładany czas BLUE: 60 minut; RED: 120 minut.
- Plan wymienia SSH, HTTP/HTTPS, UFW, Apache, ModSecurity, mod_evasive i AppArmor.
- Należy zweryfikować, czy profil AppArmor dla Apache istnieje i czy może być bezpiecznie włączony w trybie enforce.
- Zanim wyłączysz SSH, potwierdź, że nie jest wymagane do administracji/oceny; wyłącz dostęp alternatywną konsolą VM, aby nie utracić zarządzania.
