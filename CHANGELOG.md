# Sürüm geçmişi / Changelog

## 1.0.4 — 14 Kasım 2026

**Türkçe**
- Daha sade, renklerle durum gösteren Karaca Çaycı dashboard örneği.
- Kaynatma sırasında animasyon, su kaynadığında sabit durum göstergesi.
- Gereksiz kart alt yazıları kaldırıldı.
- Daha anlaşılır kurulum yönergeleri ve ana sayfadan kopyalanabilen örnek kod.

**English**
- Cleaner dashboard example with distinct active-mode colors.
- Gentle boiling animation and steady boiled-water indicator.
- Removed redundant mode-card subtitles.
- Simpler setup instructions and example code embedded on the project page.

> Yeni panel isteğe bağlıdır; mevcut Home Assistant dashboard'unuzu otomatik değiştirmez.
> The new dashboard is optional and does not automatically replace an existing Home Assistant dashboard.

---

## 1.0.3

- Küçük veri güncellemesi. / Minor data update.

## 1.0.2

- Entegrasyon kurulumunu etkileyen eksik ayarlar düzeltildi.
- Bildirim ayarlarının okunamadığı durumlar için daha güvenli yükleme eklendi.

- Fixed missing settings constants that could prevent integration setup.
- Improved safe loading when notification settings cannot be retrieved.

## 1.0.1

- Veri yenileme aralığı 10 saniyeye ayarlandı.
- Su hazır durumu `Su Kaynadı` olarak çevrildi.
- Yapılandırma akışı sorunlarına yol açan seçenek akışı kaldırıldı.

- Set the polling interval to 10 seconds.
- Translated the water-ready state to `Su Kaynadı`.
- Removed the options flow to avoid configuration errors.

## 1.0.0

- İlk sürüm: cihaz keşfi, dört çalışma modu, Türkçe durum sensörü, bildirim ve ses ayarları.
- Initial release: device discovery, four operation modes, Turkish status sensor, notification and voice settings.
