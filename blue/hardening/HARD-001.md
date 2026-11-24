---
schema: cybersparring/v0.1
type: hardening
team: blue
id: HARD-001
session_id: CS-01-S06
target_id: SRV-001
component: apache-host-hardening
status: planned
verified: false
related_test_ids: [TEST-001]
---
# HARD-001 — Plan utwardzenia hosta i Apache

## Cel i uzasadnienie
Zmniejszyć powierzchnię ataku serwera WWW, ograniczyć ruch przychodzący, ujawnić mniej informacji o serwerze oraz utrudnić modyfikację publikowanej strony przez proces serwera WWW. Jest to plan z PDF; brak potwierdzenia, że czynności wykonano.

## Stan przed zmianą
Nieudokumentowany. Przed rozpoczęciem zebrać wersję systemu/Apache, listę usług i portów oraz kopię konfiguracji bez sekretów.

## Wykonane działania / plan działań
Poniższe czynności są planem do wykonania i weryfikacji, nie opisem wykonanych zmian.

### 1. Aktualizacja i usługi (0–15 min)
Na Debian/Ubuntu w odizolowanej VM:
```bash
sudo apt update
sudo apt upgrade -y
sudo apt install apache2 ufw libapache2-mod-security2 libapache2-mod-evasive apparmor-utils -y
```
Zweryfikować, czy SSH jest wymagane. Jeżeli prowadzący zatwierdzi wyłączenie i istnieje dostęp konsolowy do VM:
```bash
sudo systemctl stop ssh
sudo systemctl disable ssh
```

### 2. Zapora UFW (15–20 min)
Przed włączeniem reguł upewnić się, że nie odetnie to wymaganej administracji. Dopuścić tylko wymagane porty serwera:
```bash
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw allow 80/tcp
# Opcjonalnie, jeśli TLS jest skonfigurowany i wymagany:
# sudo ufw allow 443/tcp
sudo ufw status verbose
sudo ufw enable
sudo ss -tulpn
```

### 3. Konfiguracja Apache (20–35 min)
Plan zakłada ograniczenie ujawniania wersji, wyłączenie zbędnych modułów i metod HTTP:
```bash
sudo a2dismod status autoindex cgi userdir -f
sudo a2enmod headers security2 evasive
```
Przykładowa konfiguracja do przeglądu przed wdrożeniem:
```apache
ServerTokens Prod
ServerSignature Off
FileETag None
TraceEnable Off

<Directory /var/www/html>
    Options -Indexes -Includes -ExecCGI -FollowSymLinks
    AllowOverride None
    <LimitExcept GET POST HEAD>
        Require all denied
    </LimitExcept>
</Directory>
```
Zapisać ją jako `/etc/apache2/conf-available/hardening.conf`, następnie:
```bash
sudo a2enconf hardening
sudo apache2ctl configtest
sudo systemctl restart apache2
```
Nie wyłączać modułów w ciemno — najpierw sprawdzić zależności i wymagania aplikacji.

### 4. Ochrona treści WWW (35–50 min)
Plan zakłada, że pliki strony nie będą zapisywalne przez `www-data`:
```bash
sudo chown -R root:root /var/www/html
sudo chmod 555 /var/www/html
sudo chmod 444 /var/www/html/index.html
sudo chattr +i /var/www/html/index.html
```
Przed zmianą potwierdzić ścieżki, zrobić kopię zapasową i sprawdzić, czy aktualizacja wdrożenia nie wymaga kontrolowanego procesu publikacji. `chattr +i` utrudnia legalne aktualizacje i musi być odwracalne w procedurze serwisowej.

AppArmor: najpierw sprawdzić dostępny profil i tryb:
```bash
sudo aa-status
```
Włączać enforce tylko po potwierdzeniu właściwego profilu i po sprawdzeniu logów odmów.

### 5. Dostęp lokalny / zmiana stanowisk (50–60 min)
PDF sugeruje ochronę GRUB hasłem i czyszczenie historii. Hasło GRUB należy skonfigurować zgodnie z dokumentacją dystrybucji i przechowywać poza repozytorium. Nie czyścić historii cudzych kont; przed przekazaniem stanowiska wylogować własną sesję i usunąć wyłącznie własne, potencjalnie wrażliwe dane zgodnie z zasadami laboratorium.

## Weryfikacja i wynik
Nie wykonano weryfikacji na podstawie dostarczonego PDF. Po wdrożeniu zapisać:
- `sudo ufw status verbose` i `sudo ss -tulpn`;
- `sudo apache2ctl configtest` oraz `sudo apache2ctl -M`;
- nagłówki HTTP oraz odpowiedzi na dozwolone i niedozwolone metody;
- właściciela/uprawnienia/atrybuty plików WWW;
- `sudo aa-status` i istotne komunikaty logów.

## Niepewności / otwarte kwestie
- Nie wskazano faktycznie użytej dystrybucji, IP, wersji ani stanu początkowego.
- Nie potwierdzono, czy SSH jest wymagane do zarządzania.
- UFW z samym portem 80 blokuje HTTPS i zdalne SSH; reguły muszą wynikać z potrzeb laboratorium.
- Sam `chattr +i` nie zastępuje kontroli procesu wdrożenia ani kopii zapasowych.
- PDF nie zawiera wyników wykonania ani dowodów.
