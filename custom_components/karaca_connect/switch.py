"""Karaca Connect Unofficial switches."""

import asyncio
import logging
import time

from homeassistant.components.switch import SwitchEntity
from homeassistant.helpers.entity import EntityCategory
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import (
    DOMAIN,
    MODE_BABY_FOOD,
    MODE_BOILING_WATER,
    MODE_FILTER_COFFEE,
    MODE_STANDBY,
    MODE_TEA_BREWING,
    SETTING_CLEANING,
    SETTING_FILTER_COFFEE_NOTIFICATION,
    SETTING_FRESHNESS,
    SETTING_NO_WATER,
    SETTING_POWER_OFF,
    SETTING_REMINDERS,
    SETTING_TEA_NOTIFICATION,
    SETTING_VOICE,
)

_LOGGER = logging.getLogger(__name__)
_last_command_time = 0

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
    try:
        settings = await api.get_settings()
    except Exception as err:
        _LOGGER.warning("Karaca settings could not be loaded: %s", err)
        settings = []
    entities = [
        KaracaModeSwitch(api, coordinator, entry, unique_id, name, mode_id, icon)
        for unique_id, name, mode_id, icon in MODE_SWITCHES
    ]
    entities.extend(
        KaracaSettingSwitch(api, entry, unique_id, name, setting_id, settings)
        for unique_id, name, setting_id in SETTING_SWITCHES
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
    """Güvenli mod switch'i."""

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
        return str(detail.get("mode")) == str(self.mode_id)

    @property
    def extra_state_attributes(self):
        detail = self.coordinator.data.get("detail", {})
        return {
            "mode_id": self.mode_id,
            "current_mode": detail.get("mode"),
            "current_mode_name": detail.get("modeName"),
            "current_state": detail.get("modeStateLabel"),
            "safe_mode": True,
            "off_sends_standby_only_if_this_mode_is_active": True,
            "author": "AzadGLR",
        }

    async def _double_refresh(self):
        await self.coordinator.async_request_refresh()
        await asyncio.sleep(1.5)
        await self.coordinator.async_request_refresh()

    def _command_allowed(self, cooldown_seconds=5):
        global _last_command_time
        now = time.time()
        if now - _last_command_time < cooldown_seconds:
            return False
        _last_command_time = now
        return True

    async def async_turn_on(self, **kwargs):
        detail = self.coordinator.data.get("detail", {})
        current_mode = detail.get("mode")
        if str(current_mode) == str(self.mode_id):
            await self._double_refresh()
            return
        if not self._command_allowed():
            await self._double_refresh()
            return
        await self.api.set_mode(self.mode_id, True)
        await self._double_refresh()

    async def async_turn_off(self, **kwargs):
        detail = self.coordinator.data.get("detail", {})
        current_mode = detail.get("mode")
        if str(current_mode) != str(self.mode_id):
            await self._double_refresh()
            return
        if not self._command_allowed():
            await self._double_refresh()
            return
        await self.api.set_mode(MODE_STANDBY, True)
        await self._double_refresh()


class KaracaSettingSwitch(KaracaBaseDevice, SwitchEntity):
    """Bildirim ve ses ayarları."""

    def __init__(self, api, entry, unique_id, name, setting_id, initial_settings):
        self.api = api
        self.entry = entry
        self.setting_id = setting_id
        self._settings = initial_settings
        self._attr_unique_id = unique_id
        self._attr_name = name
        self._attr_icon = "mdi:bell"
        self._attr_entity_category = EntityCategory.CONFIG

    @property
    def is_on(self):
        for item in self._settings:
            if item.get("id") == self.setting_id:
                return item.get("value")
        return None

    @property
    def extra_state_attributes(self):
        return {"setting_id": self.setting_id, "author": "AzadGLR"}

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
