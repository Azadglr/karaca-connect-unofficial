<p align="center">
  <img src="brand/logo.png" alt="Karaca Connect Unofficial" width="175">
</p>

<h1 align="center">Karaca Connect Unofficial</h1>
<p align="center">Karaca Çaycı cihazları için Home Assistant entegrasyonu</p>
<p align="center">
  <a href="docs/README.en.md">🇬🇧 English</a> ·
  <a href="#kurulum">Kurulum</a> ·
  <a href="#dashboard">Dashboard</a> ·
  <a href="CHANGELOG.md">Sürüm notları</a> ·
  <a href="https://github.com/Azadglr/karaca-connect-unofficial/issues">Destek</a>
</p>
<p align="center">
  <img alt="v1.0.4" src="https://img.shields.io/badge/version-1.0.4-438E78?style=flat-square">
  <img alt="Home Assistant 2025.3+" src="https://img.shields.io/badge/Home%20Assistant-2025.3%2B-41BDF5?style=flat-square">
  <img alt="MIT" src="https://img.shields.io/badge/license-MIT-68758C?style=flat-square">
</p>

> [!NOTE]
> **Bağımsız topluluk projesidir.** Karaca ile bağlantılı değildir ve Karaca tarafından desteklenmez. Kontrol için Karaca Connect bulut bağlantısı gerekir.

## Neler yapabilirsiniz?

| Mod | Desteklenen durumlar |
| --- | --- |
| ☕ **Çay Demleme** | Demleniyor, Taze Çay, Beklemiş Çay |
| ♨️ **Su Kaynatma** | Su Kaynatılıyor, Su Kaynadı |
| 🫖 **Filtre Kahve** | Kahve hazırlanıyor |
| 🍼 **Mama Suyu** | Mama suyu |

Cihaz keşfi, Türkçe durum sensörü, bildirimler, ses ve hatırlatıcı ayarları da bulunur. **Test edilen model:** Karaca Çaysever Robotea Pro Connect 4in1 (`robotea4in1`). Diğer cihazların uyumluluğu doğrulanmamıştır.

## Kurulum

[![HACS deposunu aç](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=Azadglr&repository=karaca-connect-unofficial&category=integration)

1. HACS'te **Özel depolar** bölümünden `https://github.com/Azadglr/karaca-connect-unofficial` adresini **Integration** türüyle ekleyin.
2. **Karaca Connect Unofficial** entegrasyonunu yükleyip Home Assistant'ı yeniden başlatın.
3. **Ayarlar → Cihazlar ve Hizmetler → Entegrasyon ekle** bölümünden Karaca Connect hesabınızla oturum açın.
4. Birden fazla cihaz bulunursa kullanacağınız cihazı seçin. **Karaca Çaycı** cihaz adı entegrasyon tarafından otomatik oluşturulur; elle adlandırmanız gerekmez.

<details>
<summary><strong>Manuel kurulum ve gereksinimler</strong></summary>

- [`custom_components/karaca_connect`](custom_components/karaca_connect) klasörünü `/config/custom_components/` içine kopyalayın.
- Home Assistant'ı yeniden başlatıp entegrasyonu ekleyin.
- Desteklenen asgari sürümler (HACS bildirim dosyasına göre): Home Assistant **2025.3.0**, HACS **2.0.0**.

</details>

## Dashboard

<p align="center">
  <img src="docs/images/dashboard-modern.svg" width="620" alt="Karaca Çaycı panel tasarım örneği">
</p>

Dört mod tek çerçevededir. Aktif mod renkli gösterilir; su kaynarken yumuşak animasyon, su kaynadığında sabit yeşil-turkuaz vurgu görünür. Kart altındaki gereksiz “Çalışıyor / Kapalı / Kullanılamıyor” metinleri kaldırılmıştır.

**Kart eklemek için:** HACS üzerinden [button-card](https://github.com/custom-cards/button-card) yükleyin, ardından Home Assistant'ta **Dashboard'u düzenle → Kart ekle → Manuel** adımlarını açın. Aşağıdaki kodu **bu sayfadan doğrudan** kopyalayın ve kaydedin. Ek `stack-in-card` gerekmez.

<details>
<summary><strong>📋 Animasyonlu Dashboard YAML kodunu aç ve kopyala</strong></summary>

```yaml
# Karaca Connect Unofficial - Compact animated Lovelace dashboard
# Requires HACS "button-card" custom card, NOT stack-in-card.
# Change entity IDs below if your Home Assistant installation uses different IDs.
# This visual example never hides an actual integration/cloud outage.
type: custom:button-card
show_icon: false
show_name: false
show_state: false
tap_action:
  action: none
styles:
  card:
    - padding: 7px
    - border-radius: 18px
    - background: rgba(18,21,26,.95)
    - border: 1px solid rgba(255,255,255,.085)
    - box-shadow: none
    - overflow: hidden
  grid:
    - grid-template-areas: '"header header" "tea water" "coffee baby"'
    - grid-template-columns: minmax(0,1fr) minmax(0,1fr)
    - grid-template-rows: 43px 43px 43px
    - column-gap: 7px
    - row-gap: 7px
  custom_fields:
    header:
      - width: 100%
      - min-width: 0
    tea:
      - width: 100%
      - min-width: 0
    water:
      - width: 100%
      - min-width: 0
    coffee:
      - width: 100%
      - min-width: 0
    baby:
      - width: 100%
      - min-width: 0
custom_fields:
  header:
    card:
      type: custom:button-card
      entity: sensor.karaca_cayci_durum
      name: Karaca Çaycı
      icon: mdi:kettle-steam
      show_state: true
      state_display: |
        [[[[
          const s = entity?.state ?? '';
          return !s || ['unknown','unavailable'].includes(s.toLowerCase())
            ? 'Bağlantı kontrolü' : s;
        ]]]]
      tap_action:
        action: more-info
      styles:
        card:
          - height: 43px
          - padding: 0 10px
          - border-radius: 12px
          - background: rgba(29,32,38,.94)
          - border: 1px solid rgba(255,255,255,.065)
          - box-shadow: none
        grid:
          - grid-template-areas: '"i n s"'
          - grid-template-columns: 31px minmax(0,1fr) auto
          - grid-template-rows: 1fr
          - column-gap: 9px
        img_cell:
          - width: 31px
          - height: 31px
          - border-radius: 9px
          - background: rgba(228,183,127,.12)
        icon:
          - width: 19px
          - color: '#E4B77F'
        name:
          - justify-self: start
          - font-size: 12px
          - font-weight: 500
          - color: '#EDEEF0'
        state:
          - justify-self: end
          - font-size: 10px
          - font-weight: 500
          - padding: 5px 9px
          - border-radius: 18px
          - max-width: 142px
          - overflow: hidden
          - text-overflow: ellipsis
          - white-space: nowrap
          - background: |
              [[[[
                const s = entity?.state ?? '';
                if (s === 'Su Kaynadı') return 'rgba(92,184,147,.19)';
                if (['Su Kaynatılıyor','Kaynatılıyor'].includes(s)) return 'rgba(244,147,112,.20)';
                if (['unknown','unavailable',''].includes(s.toLowerCase())) return 'rgba(198,154,75,.16)';
                return 'rgba(255,255,255,.075)';
              ]]]]
          - color: |
              [[[[
                const s = entity?.state ?? '';
                if (s === 'Su Kaynadı') return '#9DE2C8';
                if (['Su Kaynatılıyor','Kaynatılıyor'].includes(s)) return '#FFB391';
                if (['unknown','unavailable',''].includes(s.toLowerCase())) return '#E7C88E';
                return '#CBD0D8';
              ]]]]
  tea:
    card:
      type: custom:button-card
      entity: switch.karaca_cayci_cay_demleme
      name: Çay Demleme
      icon: mdi:tea
      show_state: false
      show_label: false
      tap_action:
        action: toggle
      hold_action:
        action: more-info
      styles:
        card:
          - height: 43px
          - padding: 0 10px
          - border-radius: 12px
          - box-shadow: none
          - transition: background .25s ease, border-color .25s ease
          - background: |
              [[[[
                if (entity?.state !== 'on') return 'rgba(29,33,39,.94)';
                
                return 'rgba(229,175,115,.17)';
              ]]]]
          - border: |
              [[[[
                if (entity?.state !== 'on') return '1px solid rgba(255,255,255,.075)';
                
                return '1px solid rgba(229,175,115,.36)';
              ]]]]
      
        grid:
          - grid-template-areas: '"i n"'
          - grid-template-columns: 29px minmax(0,1fr)
          - grid-template-rows: 1fr
          - column-gap: 9px
        img_cell:
          - width: 29px
          - height: 29px
          - border-radius: 9px
          - background: |
              [[[[
                return entity?.state === 'on'
                  ? 'rgba(229,175,115,.19)'
                  : 'rgba(255,255,255,.065)';
              ]]]]
        icon:
          - width: 18px
          - color: |
              [[[[
                if (entity?.state !== 'on') return '#9DA2AA';
                
                return '#E5AF73';
              ]]]]
      
        name:
          - justify-self: start
          - align-self: center
          - font-size: 11.5px
          - font-weight: 500
          - color: '#F0F2F4'
          - white-space: nowrap
  water:
    card:
      type: custom:button-card
      entity: switch.karaca_cayci_su_kaynatma
      name: Su Kaynatma
      icon: mdi:kettle-steam
      show_state: false
      show_label: false
      tap_action:
        action: toggle
      hold_action:
        action: more-info
      extra_styles: |
        @keyframes karaca-heat {
          0%, 100% { box-shadow: inset 0 0 0 1px rgba(255,126,76,.10); }
          50% { box-shadow: inset 0 0 0 1px rgba(255,166,85,.31), 0 0 11px rgba(250,113,64,.13); }
        }
        @keyframes karaca-steam {
          0%, 100% { transform: translateY(0); }
          50% { transform: translateY(-2px); }
        }
        @media (prefers-reduced-motion: reduce) {
          #card, ha-state-icon { animation: none !important; }
        }
      styles:
        card:
          - height: 43px
          - padding: 0 10px
          - border-radius: 12px
          - box-shadow: none
          - transition: background .25s ease, border-color .25s ease
          - background: |
              [[[[
                if (entity?.state !== 'on') return 'rgba(29,33,39,.94)';
                if (entity?.state === 'on' && states['sensor.karaca_cayci_durum']?.state === 'Su Kaynadı') return 'rgba(43,103,87,.36)';
                return 'rgba(244,143,105,.17)';
              ]]]]
          - border: |
              [[[[
                if (entity?.state !== 'on') return '1px solid rgba(255,255,255,.075)';
                if (entity?.state === 'on' && states['sensor.karaca_cayci_durum']?.state === 'Su Kaynadı') return '1px solid rgba(119,213,183,.40)';
                return '1px solid rgba(244,143,105,.36)';
              ]]]]
          - animation: |
              [[[[
                return entity?.state === 'on' && ['Su Kaynatılıyor', 'Kaynatılıyor'].includes(states['sensor.karaca_cayci_durum']?.state) ? 'karaca-heat 2.3s ease-in-out infinite' : 'none';
              ]]]]
        grid:
          - grid-template-areas: '"i n"'
          - grid-template-columns: 29px minmax(0,1fr)
          - grid-template-rows: 1fr
          - column-gap: 9px
        img_cell:
          - width: 29px
          - height: 29px
          - border-radius: 9px
          - background: |
              [[[[
                return entity?.state === 'on'
                  ? 'rgba(244,143,105,.19)'
                  : 'rgba(255,255,255,.065)';
              ]]]]
        icon:
          - width: 18px
          - color: |
              [[[[
                if (entity?.state !== 'on') return '#9DA2AA';
                if (entity?.state === 'on' && states['sensor.karaca_cayci_durum']?.state === 'Su Kaynadı') return '#88DDC5';
                return '#F48F69';
              ]]]]
          - animation: |
              [[[[
                return entity?.state === 'on' && ['Su Kaynatılıyor', 'Kaynatılıyor'].includes(states['sensor.karaca_cayci_durum']?.state) ? 'karaca-steam 1.6s ease-in-out infinite' : 'none';
              ]]]]
        name:
          - justify-self: start
          - align-self: center
          - font-size: 11.5px
          - font-weight: 500
          - color: '#F0F2F4'
          - white-space: nowrap
  coffee:
    card:
      type: custom:button-card
      entity: switch.karaca_cayci_filtre_kahve
      name: Filtre Kahve
      icon: mdi:coffee-maker
      show_state: false
      show_label: false
      tap_action:
        action: toggle
      hold_action:
        action: more-info
      styles:
        card:
          - height: 43px
          - padding: 0 10px
          - border-radius: 12px
          - box-shadow: none
          - transition: background .25s ease, border-color .25s ease
          - background: |
              [[[[
                if (entity?.state !== 'on') return 'rgba(29,33,39,.94)';
                
                return 'rgba(215,160,137,.17)';
              ]]]]
          - border: |
              [[[[
                if (entity?.state !== 'on') return '1px solid rgba(255,255,255,.075)';
                
                return '1px solid rgba(215,160,137,.36)';
              ]]]]
      
        grid:
          - grid-template-areas: '"i n"'
          - grid-template-columns: 29px minmax(0,1fr)
          - grid-template-rows: 1fr
          - column-gap: 9px
        img_cell:
          - width: 29px
          - height: 29px
          - border-radius: 9px
          - background: |
              [[[[
                return entity?.state === 'on'
                  ? 'rgba(215,160,137,.19)'
                  : 'rgba(255,255,255,.065)';
              ]]]]
        icon:
          - width: 18px
          - color: |
              [[[[
                if (entity?.state !== 'on') return '#9DA2AA';
                
                return '#D7A089';
              ]]]]
      
        name:
          - justify-self: start
          - align-self: center
          - font-size: 11.5px
          - font-weight: 500
          - color: '#F0F2F4'
          - white-space: nowrap
  baby:
    card:
      type: custom:button-card
      entity: switch.karaca_cayci_mama_suyu
      name: Mama Suyu
      icon: mdi:baby-bottle
      show_state: false
      show_label: false
      tap_action:
        action: toggle
      hold_action:
        action: more-info
      styles:
        card:
          - height: 43px
          - padding: 0 10px
          - border-radius: 12px
          - box-shadow: none
          - transition: background .25s ease, border-color .25s ease
          - background: |
              [[[[
                if (entity?.state !== 'on') return 'rgba(29,33,39,.94)';
                
                return 'rgba(159,208,179,.17)';
              ]]]]
          - border: |
              [[[[
                if (entity?.state !== 'on') return '1px solid rgba(255,255,255,.075)';
                
                return '1px solid rgba(159,208,179,.36)';
              ]]]]
      
        grid:
          - grid-template-areas: '"i n"'
          - grid-template-columns: 29px minmax(0,1fr)
          - grid-template-rows: 1fr
          - column-gap: 9px
        img_cell:
          - width: 29px
          - height: 29px
          - border-radius: 9px
          - background: |
              [[[[
                return entity?.state === 'on'
                  ? 'rgba(159,208,179,.19)'
                  : 'rgba(255,255,255,.065)';
              ]]]]
        icon:
          - width: 18px
          - color: |
              [[[[
                if (entity?.state !== 'on') return '#9DA2AA';
                
                return '#9FD0B3';
              ]]]]
      
        name:
          - justify-self: start
          - align-self: center
          - font-size: 11.5px
          - font-weight: 500
          - color: '#F0F2F4'
          - white-space: nowrap
```

**Not:** Cihazınızın varlık kimlikleri farklıysa `sensor.karaca_cayci_durum` ve dört `switch.karaca_cayci_...` satırını kendi kimliklerinizle eşleştirin. Bu örnek yalnızca görsel karttır; entegrasyon normal Home Assistant kartlarıyla da çalışır.

</details>

<details>
<summary><strong>Diğer ekran görüntülerini göster</strong></summary>

| Cihaz kontrolleri | Bildirim ve ses ayarları |
| :---: | :---: |
| <img src="docs/images/device-page.png" width="310" alt="Cihaz sayfası"> | <img src="docs/images/config-page.png" width="310" alt="Bildirim ayarları"> |
| İlk kurulum | |
| <img src="docs/images/setup-flow.png" width="310" alt="Kurulum ekranı"> | |

</details>

## 1.0.4 güncellemesinde neler düzeldi?

- Dashboard'da gereksiz **“Kullanılamıyor”** alt yazısı kaldırıldı; mod durumu renklerle gösteriliyor.
- Su kaynatma ve su kaynadı görünümleri ayrıştırıldı; kompakt animasyonlu kart örneği eklendi.
- Türkçe ve İngilizce açıklamalar, kurulum ve örnek kod güncellendi.
- Entegrasyon sürüm bilgileri 1.0.4 olarak eşitlendi.

> Bu bir **arayüz/dokümantasyon düzenlemesidir**. Karaca bulutundaki gerçek ağ veya API kesintileri giderilmiş gibi sunulmaz.

**Çalışma bilgisi:** Durumlar yaklaşık 10 saniyede bir sorgulanır. Mod geçişlerinde 5 saniyelik komut koruması bulunur. Çay tazeliği etiketleri cihaz verisinden gelir; entegrasyonda bağımsız bir 1 saatlik sayaç yoktur.

## Destek ve lisans

Hata ve öneriler: [GitHub Issues](https://github.com/Azadglr/karaca-connect-unofficial/issues) · [GitHub Sponsors](https://github.com/sponsors/Azadglr) · [ByNoGame](https://donate.bynogame.com/azadglr).

Paylaşılan hata kayıtlarından parolaları, erişim anahtarlarını ve cihaz kimliklerini çıkarın. Proje [MIT Lisansı](LICENSE) ile sunulur. Bu yazılım resmî Karaca hizmeti değildir.

**Güncel sürüm: v1.0.4.**
