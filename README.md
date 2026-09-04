# Exchange Rate Scraper

A small web scraping script built with **Playwright** that fetches live USD and EUR exchange rates (in Turkish Lira) from doviz.com.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Playwright](https://img.shields.io/badge/Playwright-Web%20Automation-green)

---

## 🇬🇧 English

### Overview
This script launches a headless browser, navigates to doviz.com, and extracts the current USD and EUR exchange rates against the Turkish Lira by reading specific elements on the page.

### Features
- Headless browser automation via Playwright
- Fetches multiple currencies from a simple, extensible dictionary
- Graceful error handling for slow connections or page structure changes
- Clean, formatted console output

### Requirements
- Python 3.10 or higher
- `playwright`

### Installation
```bash
pip install playwright
playwright install chromium
```
> The second command downloads the Chromium browser binary that Playwright controls — this is required even if Chrome is already installed on your system.

### Usage
```bash
python exchange_rate_scraper.py
```

### How it works
Playwright launches a headless Chromium instance and navigates to the target page. `page.wait_for_selector()` waits for a specific `<span>` element (identified by a `data-socket-key` attribute matching the currency code) to appear before reading its text with `page.inner_text()`. Since websites can change their HTML structure at any time, each currency lookup is wrapped in its own timeout handler — if a selector isn't found within 10 seconds, the script reports that currency as unavailable instead of crashing.

### Notes
- This script depends on doviz.com's current page structure (specifically the `data-socket-key` attribute). If the site changes its layout, the selectors may need to be updated.
- Intended for personal, educational use — check a site's terms of service before scraping it for other purposes.
- Note: This project was developed with AI assistance as part of my learning process.

---

## 🇩🇪 Deutsch

### Überblick
Dieses Skript startet einen Headless-Browser, navigiert zu doviz.com und extrahiert die aktuellen USD- und EUR-Wechselkurse gegenüber der türkischen Lira, indem es bestimmte Elemente auf der Seite ausliest.

### Funktionen
- Headless-Browser-Automatisierung über Playwright
- Ruft mehrere Währungen aus einem einfachen, erweiterbaren Dictionary ab
- Robuste Fehlerbehandlung bei langsamen Verbindungen oder Änderungen der Seitenstruktur
- Übersichtliche, formatierte Konsolenausgabe

### Voraussetzungen
- Python 3.10 oder höher
- `playwright`

### Installation
```bash
pip install playwright
playwright install chromium
```
> Der zweite Befehl lädt die Chromium-Browser-Binärdatei herunter, die von Playwright gesteuert wird — dies ist erforderlich, auch wenn Chrome bereits auf deinem System installiert ist.

### Verwendung
```bash
python exchange_rate_scraper.py
```

### Funktionsweise
Playwright startet eine Headless-Chromium-Instanz und navigiert zur Zielseite. `page.wait_for_selector()` wartet darauf, dass ein bestimmtes `<span>`-Element (identifiziert durch ein `data-socket-key`-Attribut, das dem Währungscode entspricht) erscheint, bevor dessen Text mit `page.inner_text()` ausgelesen wird. Da Websites ihre HTML-Struktur jederzeit ändern können, ist jede Währungsabfrage in einen eigenen Timeout-Handler eingebettet — wird ein Selektor nicht innerhalb von 10 Sekunden gefunden, meldet das Skript diese Währung als nicht verfügbar, anstatt abzustürzen.

### Hinweise
- Dieses Skript ist von der aktuellen Seitenstruktur von doviz.com abhängig (insbesondere dem `data-socket-key`-Attribut). Ändert die Seite ihr Layout, müssen die Selektoren möglicherweise aktualisiert werden.
- Für den persönlichen, edukativen Gebrauch gedacht — prüfe die Nutzungsbedingungen einer Website, bevor du sie für andere Zwecke scrapst.
- Hinweis: Dieses Projekt wurde im Rahmen meines Lernprozesses mit KI-Unterstützung entwickelt.

---

## 🇹🇷 Türkçe

### Genel Bakış
Bu script, headless (arayüzsüz) bir tarayıcı başlatır, doviz.com'a gider ve sayfadaki belirli elementleri okuyarak güncel USD ve EUR kurlarını (Türk Lirası karşısında) çeker.

### Özellikler
- Playwright üzerinden headless tarayıcı otomasyonu
- Basit, genişletilebilir bir dictionary'den birden fazla para birimi çekme
- Yavaş bağlantılar veya sayfa yapısı değişiklikleri için zarif hata yönetimi
- Sade, biçimlendirilmiş konsol çıktısı

### Gereksinimler
- Python 3.10 veya üzeri
- `playwright`

### Kurulum
```bash
pip install playwright
playwright install chromium
```
> İkinci komut, Playwright'ın kontrol ettiği Chromium tarayıcı ikili dosyasını indirir — sisteminde Chrome kurulu olsa bile bu gereklidir.

### Kullanım
```bash
python exchange_rate_scraper.py
```

### Nasıl çalışır?
Playwright, headless bir Chromium örneği başlatır ve hedef sayfaya gider. `page.wait_for_selector()`, belirli bir `<span>` elementinin (para birimi koduyla eşleşen bir `data-socket-key` özniteliğiyle tanımlanan) belirmesini bekler, ardından metnini `page.inner_text()` ile okur. Web siteleri HTML yapılarını her an değiştirebildiği için, her para birimi sorgusu kendi timeout işleyicisine sarılmıştır — bir seçici 10 saniye içinde bulunamazsa, script çökmek yerine o para birimini "mevcut değil" olarak bildirir.

### Notlar
- Bu script, doviz.com'un mevcut sayfa yapısına (özellikle `data-socket-key` özniteliğine) bağımlıdır. Site düzenini değiştirirse, seçicilerin güncellenmesi gerekebilir.
- Kişisel, eğitim amaçlı kullanım için tasarlanmıştır — başka amaçlarla scrape etmeden önce bir sitenin kullanım şartlarını kontrol et.
- Not: Bu proje, öğrenme sürecimin bir parçası olarak yapay zeka desteğiyle geliştirilmiştir.
