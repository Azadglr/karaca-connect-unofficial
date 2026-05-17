# Karaca Connect Unofficial

Unofficial Home Assistant integration for compatible Karaca Connect devices.

> This project is not affiliated with, endorsed by, or supported by Karaca.

## 🇹🇷 Türkçe

**Karaca Connect Unofficial**, Karaca Connect uygulamasıyla çalışan uyumlu cihazları Home Assistant üzerinden kontrol etmek için geliştirilmiş resmi olmayan bir Home Assistant entegrasyonudur.

### Özellikler

- Çay Demleme
- Su Kaynatma
- Filtre Kahve
- Mama Suyu
- Türkçe durum sensörü
- Otomatik cihaz keşfi
- Bildirim ve konuşma sesi ayarları
- Güvenli switch davranışı
- Home Assistant cihaz sayfasında temiz kontrol görünümü

### Test Edilen Cihaz

- Karaca Çaysever Robotea Pro Connect 4in1
- Device type: `robotea4in1`

## 🇬🇧 English

**Karaca Connect Unofficial** is an unofficial Home Assistant integration for compatible Karaca Connect devices.

### Features

- Tea Brewing
- Boiling Water
- Filter Coffee
- Baby Water
- Turkish status sensor
- Automatic device discovery
- Notification and voice settings
- Safe switch behavior
- Clean Home Assistant device page controls

### Tested Device

- Karaca Çaysever Robotea Pro Connect 4in1
- Device type: `robotea4in1`

## 📸 Screenshots / Ekran Görüntüleri

### Dashboard
![Dashboard](docs/images/dashboard.png)

### Device Page / Cihaz Sayfası
![Device Page](docs/images/device-page.png)

### Configuration / Yapılandırma
![Configuration](docs/images/config-page.png)

### Setup Flow / Kurulum Ekranı
![Setup Flow](docs/images/setup-flow.png)

## 📦 Installation / Kurulum

[![Open your Home Assistant instance and open this repository in HACS.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=Azadglr&repository=karaca-connect-unofficial&category=integration)

### Manual Installation / Manuel Kurulum

- Copy the `karaca_connect` folder into `/config/custom_components/`.
- Restart Home Assistant.
- Go to **Settings → Devices & Services → Add Integration**.
- Search for **Karaca Connect Unofficial**.
- Enter your Karaca Connect account information.
- Select your device if multiple devices are found.

### HACS Custom Repository

If the repository is public or accessible to your GitHub account, add it as a custom repository in HACS:

```text
https://github.com/Azadglr/karaca-connect-unofficial
```

Category:

```text
Integration
```

## 🎛️ Controls / Kontroller

After installation, the device page shows four main switches:

Kurulumdan sonra cihaz sayfasında dört ana switch görünür:

- Çay Demleme / Tea Brewing
- Su Kaynatma / Boiling Water
- Filtre Kahve / Filter Coffee
- Mama Suyu / Baby Water

### Safe switch behavior / Güvenli switch davranışı

- Switch **ON** starts the selected mode.
- Switch **OFF** only sends standby if that exact mode is currently active.
- If another mode is active, switch OFF does nothing.
- Commands include cooldown protection to reduce accidental repeated API calls.

## ⚙️ Configuration / Yapılandırma

Notification and voice settings are shown under the device **Configuration** section.

Bildirim ve konuşma sesi ayarları cihazın **Yapılandırma** bölümünde görünür.

Available settings:

- Çay Demleme Bildirimi
- Filtre Kahve Bildirimi
- Tazelik Bildirimi
- Kapanma Bildirimi
- Su Kalmadı Bildirimi
- Anımsatıcı Bildirimler
- Konuşma Sesi
- Temizlik Bildirimi

## ❤️ Support / Destek

Bu proje işinize yarıyorsa geliştirmeyi destekleyebilirsiniz.

If this project is useful for you, you can support development.

- 💖 GitHub Sponsors: https://github.com/sponsors/Azadglr
- 🎮 ByNoGame: https://donate.bynogame.com/azadglr
- 📧 Contact: azadgulerr@gmail.com

## 🔖 Version / Sürüm

`1.0.0`

## 🔒 License / Lisans

It may not be copied, redistributed, resold, published, modified, or shared without permission.

İzinsiz kopyalanamaz, dağıtılamaz, satılamaz, yayınlanamaz, değiştirilemez veya paylaşılamaz.

See: [LICENSE](LICENSE)

## ⚠️ Disclaimer / Uyarı

This project is not affiliated with Karaca.
It is not developed, supported, or endorsed by Karaca.
If the Karaca Connect cloud API changes, this integration may stop working or require updates.
Use at your own risk.

Bu proje Karaca ile bağlantılı değildir.
Karaca tarafından geliştirilmemiş, desteklenmemiş veya onaylanmamıştır.
Karaca Connect bulut API’si değişirse entegrasyonun çalışması etkilenebilir.
Kullanım sorumluluğu kullanıcıya aittir.