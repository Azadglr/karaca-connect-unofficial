"""
Karaca Connect Home Assistant Integration
Private local integration developed by AzadGLR.

Author: AzadGLR
Signature: by AzadGLR
Owner: AzadGLR
Version: 1.0.0
"""

import asyncio

from homeassistant.components.switch import SwitchEntity
from homeassistant.helpers.entity import EntityCategory
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import (
    DOMAIN,
    MODE_STANDBY,
    MODE_TEA_BREWING,
    MODE_BOILING_WATER,
    MODE_FILTER_COFFEE,
    MODE_BABY_FOOD,
    SETTING_TEA_NOTIFICATION,
    SETTING_FILTER_COFFEE_NOTIFICATION,
    SETTING_FRESHNESS,
    SETTING_POWER_OFF,
    SETTING_NO_WATER,
    SETTING_REMINDERS,
    SETTING_VOICE,
    SETTING_CLEANING,
)


MODE_SWITCHES = [
    ("karaca_cay_demleme", "Çay Demleme", MODE_TEA_BREWING, "mdi:tea"),
    ("karaca_su_kaynatma", "Su Kaynatma", MODE_BOILING_WATER, "mdi:kettle"),
    ("karaca_filtre_kahve", "Filtre Kahve", MODE_FILTER_COFFEE, "mdi:coffee-maker"),
    ("karaca_mama_suyu", "Mama Suyu", MODE_BABY_FOOD, "mdi:baby-bottle"),
]


SETTING_SWITCHES = [
    ("karaca_cay_demleme_bildirimi", "Çay Demleme Bildirimi", SETTING_TEA_NOTIFICATION),
    ("karaca_filtre_kahve_bildirimi", "Filtre Kahve Bildirimi", SETTING_FILTER_COFFEE_NOTIFICATION),
    ("karaca_tazelik_bildirimi", "Tazelik Bildirimi", SETTING_FRESHNESS),
    ("karaca_kapanma_bildirimi", "Kapanma Bildirimi", SETTING_POWER_OFF),
    ("karaca_su_kalmadi_bildirimi", "Su Kalmadı Bildirimi", SETTING_NO_WATER),
    ("karaca_animsatici_bildirimler", "Anımsatıcı Bildirimler", SETTING_REMINDERS),
    ("karaca_konusma_sesi", "Konuşma Sesi", SETTING_VOICE),
    ("karaca_temizlik_bildirimi", "Temizlik Bildirimi", SETTING_CLEANING),
]


async def async_setup_entry(hass, entry, async_add_entities):
    data = hass.data[DOMAIN][entry.entry_id]
    api = data["api"]
    coordinator = data["coordinator"]

    settings = await api.get_settings()

    entities = []

    # Ana 4 mod switch'i: Kontroller bölümünde görünür
    for unique_id, name, mode_id, icon in MODE_SWITCHES:
        entities.append(
            KaracaModeSwitch(
                api=api,
                coordinator=coordinator,
                entry=entry,
                unique_id=unique_id,
                name=name,
                mode_id=mode_id,
                icon=icon,
            )
        )

    # Bildirim / ses ayarları: Yapılandırma bölümünde görünür
    for unique_id, name, setting_id in SETTING_SWITCHES:
        entities.append(
            KaracaSettingSwitch(
                api=api,
                entry=entry,
                unique_id=unique_id,
                name=name,
                setting_id=setting_id,
                initial_settings=settings,
            )
        )

    async_add_entities(entities)


class KaracaBaseDevice:
    @property
    def device_info(self):
        return {
            "identifiers": {(DOMAIN, self.entry.entry_id)},
            "name": "Karaca Çaycı",
            "manufacturer": "AzadGLR",
            "model": "Çaysever Robotea Pro Connect 4in1",
        }


class KaracaModeSwitch(KaracaBaseDevice, CoordinatorEntity, SwitchEntity):
    """
    Ana mod switch'i.

    Aynı anda sadece 1 mod açık görünür.
    Çünkü state cihazın gerçek mode değerinden okunur.

    ON:
      Hedef modu başlatır.

    OFF:
      Eğer bu mod aktifse standby mode ID=1 gönderir.
    """

    def __init__(self, api, coordinator, entry, unique_id, name, mode_id, icon):
        super().__init__(coordinator)

        self.api = api
        self.entry = entry
        self.mode_id = mode_id

        self._attr_unique_id = unique_id
        self._attr_name = name
        self._attr_icon = icon

    @property
    def is_on(self):
        detail = self.coordinator.data.get("detail", {})
        current_mode = detail.get("mode")

        return str(current_mode) == str(self.mode_id)

    @property
    def extra_state_attributes(self):
        detail = self.coordinator.data.get("detail", {})

        return {
            "mode_id": self.mode_id,
            "current_mode": detail.get("mode"),
            "current_mode_name": detail.get("modeName"),
            "current_state": detail.get("modeStateLabel"),
            "author": "AzadGLR",
            "signature": "by AzadGLR",
        }

    async def _double_refresh(self):
        """
        Karaca API bazen mode bilgisini hemen,
        modeStateLabel bilgisini ise gecikmeli güncelliyor.

        Bu yüzden:
        1. hemen refresh
        2. 1.5 saniye sonra tekrar refresh
        """
        await self.coordinator.async_request_refresh()
        await asyncio.sleep(1.5)
        await self.coordinator.async_request_refresh()

    async def async_turn_on(self, **kwargs):
        # Başka mod açıksa cihaz tarafı zaten tek moda geçiyor.
        # Refresh sonrası diğer switch'ler OFF görünür.
        await self.api.set_mode(self.mode_id, True)
        await self._double_refresh()

    async def async_turn_off(self, **kwargs):
        # Sadece bu mod aktifse standby'a al.
        detail = self.coordinator.data.get("detail", {})
        current_mode = detail.get("mode")

        if str(current_mode) == str(self.mode_id):
            await self.api.set_mode(MODE_STANDBY, True)

        await self._double_refresh()


class KaracaSettingSwitch(KaracaBaseDevice, SwitchEntity):
    """
    Bildirim / ses ayarları.

    EntityCategory.CONFIG sayesinde Kontroller altında değil,
    cihaz sayfasındaki Yapılandırma bölümünde görünür.
    """

    def __init__(self, api, entry, unique_id, name, setting_id, initial_settings):
        self.api = api
        self.entry = entry
        self.setting_id = setting_id
        self._settings = initial_settings

        self._attr_unique_id = unique_id
        self._attr_name = name
        self._attr_icon = "mdi:bell"

        # Ayar switch'leri Kontroller yerine Yapılandırma altında görünür.
        self._attr_entity_category = EntityCategory.CONFIG

    @property
    def is_on(self):
        for item in self._settings:
            if item.get("id") == self.setting_id:
                return item.get("value")

        return None

    @property
    def extra_state_attributes(self):
        return {
            "setting_id": self.setting_id,
            "author": "AzadGLR",
            "signature": "by AzadGLR",
        }

    async def async_turn_on(self, **kwargs):
        await self.api.set_setting(self.setting_id, True)
        self._settings = await self.api.get_settings()
        self.async_write_ha_state()

    async def async_turn_off(self, **kwargs):
        await self.api.set_setting(self.setting_id, False)
        self._settings = await self.api.get_settings()
        self.async_write_ha_state()

    async def async_update(self):
        self._settings = await self.api.get_settings()