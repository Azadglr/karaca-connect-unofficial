# Karaca Connect Unofficial

Unofficial Home Assistant integration for Karaca Connect devices.

Developed by **AzadGLR**.

> This project is not affiliated with, endorsed by, or supported by Karaca.

---

## 🇹🇷 Türkçe

**Karaca Connect Unofficial**, Karaca Connect uygulamasıyla çalışan uyumlu cihazları Home Assistant üzerinden kontrol etmek için geliştirilmiş resmi olmayan bir Home Assistant entegrasyonudur.

Bu entegrasyon ile desteklenen cihazlarda şu işlemler yapılabilir:

- Çay Demleme
- Su Kaynatma
- Filtre Kahve
- Mama Suyu
- Cihaz durumunu görüntüleme
- Bildirim ve konuşma sesi ayarlarını yönetme

Bu entegrasyon resmi Karaca ürünü değildir. Karaca tarafından geliştirilmemiş, desteklenmemiş veya onaylanmamıştır.

---

## 🇬🇧 English

**Karaca Connect Unofficial** is an unofficial Home Assistant integration for compatible Karaca Connect devices.

With this integration, supported devices can be controlled from Home Assistant:

- Tea Brewing
- Boiling Water
- Filter Coffee
- Baby Water
- Device status monitoring
- Notification and voice setting controls

This integration is not an official Karaca product. It is not developed, supported, or endorsed by Karaca.

---

## ✨ Özellikler / Features

### 🇹🇷 Türkçe

- Home Assistant arayüzünden cihaz kontrolü
- Otomatik cihaz keşfi
- 4 mod için switch kontrolü
- Aynı anda yalnızca bir mod aktif olacak şekilde çalışma
- Türkçe durum sensörü
- Bildirim ve konuşma sesi ayarları
- Ayarların cihaz sayfasında **Yapılandırma** bölümünde görünmesi
- Lokal logo/icon desteği
- Home Assistant kurulum ekranı desteği

### 🇬🇧 English

- Device control from Home Assistant
- Automatic device discovery
- Switch control for 4 device modes
- Only one mode can be active at a time
- Turkish status sensor
- Notification and voice setting controls
- Settings shown under the **Configuration** section of the device page
- Local logo/icon support
- Home Assistant UI setup flow

---

## ✅ Desteklenen Cihazlar / Supported Devices

### 🇹🇷 Türkçe

Test edilen cihaz:

- Karaca Çaysever Robotea Pro Connect 4in1
- Device type: `robotea4in1`

Diğer Karaca Connect cihazları henüz test edilmemiştir.

### 🇬🇧 English

Tested device:

- Karaca Çaysever Robotea Pro Connect 4in1
- Device type: `robotea4in1`

Other Karaca Connect devices have not been tested yet.

---

## 📸 Ekran Görüntüleri / Screenshots

> Not: Görseller `docs/images/` klasörü altında tutulur.

### Dashboard

![Dashboard](docs/images/dashboard.png)

### Cihaz Sayfası / Device Page

![Device Page](docs/images/device-page.png)

### Yapılandırma / Configuration

![Configuration](docs/images/config-page.png)

### Kurulum Ekranı / Setup Flow

![Setup Flow](docs/images/setup-flow.png)

---

## 📦 Kurulum / Installation

### 🇹🇷 Türkçe

Bu entegrasyon özel/ücretli dağıtım içindir.

#### Manuel Kurulum

1. ZIP dosyasını açın.

2. ZIP dosyasının içinden çıkan `karaca_connect` klasörünü bulun.

3. `karaca_connect` klasörünü Home Assistant içinde şu klasöre kopyalayın:

```text
/config/custom_components/
```

4. Son klasör yapısı şu şekilde olmalıdır:

```text
/config/custom_components/karaca_connect/
```

5. `karaca_connect` klasörünün içinde aşağıdaki dosyalar ve klasörler bulunmalıdır:

```text
karaca_connect/
├── brand/
├── translations/
├── __init__.py
├── api.py
├── config_flow.py
├── const.py
├── manifest.json
├── sensor.py
├── switch.py
└── strings.json
```

6. Home Assistant’ı yeniden başlatın.

Home Assistant arayüzünden:

```text
Ayarlar → Sistem → Yeniden Başlat
```

veya terminalden:

```bash
ha core restart
```

7. Home Assistant yeniden açıldıktan sonra şu menüye gidin:

```text
Ayarlar → Cihazlar ve Hizmetler → Entegrasyon Ekle
```

8. Arama kutusuna şunu yazın:

```text
Karaca Connect Unofficial
```

9. Entegrasyonu seçin.

10. Karaca Connect hesabınıza ait bilgileri girin:

```text
E-posta
Şifre
```

11. Eğer hesabınızda tek cihaz varsa cihaz otomatik olarak seçilir.

12. Eğer hesabınızda birden fazla cihaz varsa listeden kullanmak istediğiniz cihazı seçin.

13. Kurulum tamamlandıktan sonra cihaz sayfasında şu kontroller görünür:

```text
Çay Demleme
Su Kaynatma
Filtre Kahve
Mama Suyu
```

14. Cihazın çalışma bilgisi için şu sensör görünür:

```text
Durum
```

15. Bildirim ve konuşma sesi gibi ayarlar cihaz sayfasında **Yapılandırma** bölümünde görünür.

---

### 🇬🇧 English

This integration is currently distributed as private paid software.

#### Manual Installation

1. Extract the ZIP file.

2. Find the `karaca_connect` folder inside the ZIP file.

3. Copy the `karaca_connect` folder into the following Home Assistant directory:

```text
/config/custom_components/
```

4. The final folder structure should be:

```text
/config/custom_components/karaca_connect/
```

5. The `karaca_connect` folder should contain the following files and folders:

```text
karaca_connect/
├── brand/
├── translations/
├── __init__.py
├── api.py
├── config_flow.py
├── const.py
├── manifest.json
├── sensor.py
├── switch.py
└── strings.json
```

6. Restart Home Assistant.

From the Home Assistant UI:

```text
Settings → System → Restart
```

or from the terminal:

```bash
ha core restart
```

7. After Home Assistant restarts, go to:

```text
Settings → Devices & Services → Add Integration
```

8. Search for:

```text
Karaca Connect Unofficial
```

9. Select the integration.

10. Enter your Karaca Connect account information:

```text
Email
Password
```

11. If only one device is found, it will be selected automatically.

12. If multiple devices are found, select the device you want to use.

13. After setup is complete, the device page will show the following controls:

```text
Tea Brewing
Boiling Water
Filter Coffee
Baby Water
```

14. The device status will be shown with the following sensor:

```text
Status
```

15. Notification and voice settings will appear under the **Configuration** section of the device page.

---

## 🎛️ Kullanım / Usage

### 🇹🇷 Türkçe

Kurulumdan sonra cihaz sayfasında şu kontroller görünür:

- Çay Demleme
- Su Kaynatma
- Filtre Kahve
- Mama Suyu

Mod kontrolleri switch olarak çalışır.

Örnek kullanım:

- `Çay Demleme` açılırsa çay demleme modu başlar.
- `Su Kaynatma` açılırsa su kaynatma modu başlar.
- `Filtre Kahve` açılırsa filtre kahve modu başlar.
- `Mama Suyu` açılırsa mama suyu modu başlar.
- Açık olan mod switch’i kapatılırsa cihaz standby/kapalı moda alınır.
- Başka bir mod açılırsa önceki mod otomatik olarak pasif görünür.

Aynı anda yalnızca bir mod aktif olabilir.

### 🇬🇧 English

After installation, the following controls will appear on the device page:

- Tea Brewing
- Boiling Water
- Filter Coffee
- Baby Water

Mode controls work as switches.

Example usage:

- Turning on `Tea Brewing` starts tea brewing mode.
- Turning on `Boiling Water` starts boiling water mode.
- Turning on `Filter Coffee` starts filter coffee mode.
- Turning on `Baby Water` starts baby water mode.
- Turning off the active mode switch puts the device into standby/off mode.
- Turning on another mode automatically makes the previous mode appear inactive.

Only one mode can be active at a time.

---

## ⚙️ Bildirim ve Ses Ayarları / Notification and Voice Settings

### 🇹🇷 Türkçe

Aşağıdaki ayarlar cihazın **Yapılandırma** bölümünde görünür:

- Çay Demleme Bildirimi
- Filtre Kahve Bildirimi
- Tazelik Bildirimi
- Kapanma Bildirimi
- Su Kalmadı Bildirimi
- Anımsatıcı Bildirimler
- Konuşma Sesi
- Temizlik Bildirimi

Bu ayarlar cihaz sayfasında ayrı switch olarak görünür, ancak normal kontrol alanında değil **Yapılandırma** bölümünde yer alır.

### 🇬🇧 English

The following settings are shown under the device **Configuration** section:

- Tea Brewing Notification
- Filter Coffee Notification
- Freshness Notification
- Power Off Notification
- No Water Notification
- Reminder Notifications
- Voice
- Cleaning Notification

These settings appear as switches on the device page, but they are placed under the **Configuration** section instead of the main controls area.

---

## 🔖 Sürüm / Version

```text
1.0.0
```

---

## 🔒 Lisans / License

### 🇹🇷 Türkçe

Bu yazılım özel/ücretli yazılımdır.

İzinsiz olarak:

- Kopyalanamaz
- Dağıtılamaz
- Satılamaz
- Paylaşılamaz
- Yayınlanamaz
- Değiştirilip yeniden dağıtılamaz

Detaylar için:

```text
PRIVATE_LICENSE.md
```

### 🇬🇧 English

This software is private paid software.

It may not be:

- Copied
- Redistributed
- Resold
- Shared
- Published
- Modified and redistributed

See:

```text
PRIVATE_LICENSE.md
```

---

## ⚠️ Uyarı / Disclaimer

### 🇹🇷 Türkçe

Bu proje Karaca ile bağlantılı değildir.

Karaca tarafından geliştirilmemiş, desteklenmemiş veya onaylanmamıştır.

Karaca Connect bulut API’si değişirse entegrasyonun çalışması etkilenebilir.

Kullanım sorumluluğu kullanıcıya aittir.

### 🇬🇧 English

This project is not affiliated with Karaca.

It is not developed, supported, or endorsed by Karaca.

If the Karaca Connect cloud API changes, this integration may stop working or require updates.

Use at your own risk.