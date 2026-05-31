"""Karaca Connect Unofficial sensors."""

from homeassistant.components.sensor import SensorEntity
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN, translate_state


async def async_setup_entry(hass, entry, async_add_entities):
    data = hass.data[DOMAIN][entry.entry_id]
    async_add_entities([KaracaStatusSensor(data["coordinator"], entry)])


class KaracaBaseSensor(CoordinatorEntity, SensorEntity):
    def __init__(self, coordinator, entry):
        super().__init__(coordinator)
        self.entry = entry
        self._attr_device_info = {
            "identifiers": {(DOMAIN, entry.entry_id)},
            "name": "Karaca Çaycı",
            "manufacturer": "AzadGLR",
            "model": "Çaysever Robotea Pro Connect 4in1",
        }


class KaracaStatusSensor(KaracaBaseSensor):
    """Tek durum sensörü."""

    _attr_name = "Durum"
    _attr_unique_id = "karaca_cayci_durum"
    _attr_icon = "mdi:kettle-pour-over"

    @property
    def native_value(self):
        detail = self.coordinator.data.get("detail", {})

        mode = detail.get("mode")
        mode_name = detail.get("modeName")
        mode_state_label = detail.get("modeStateLabel")

        if str(mode) == "1":
            return "Kapalı"

        if mode_state_label not in (None, "", "off", "standby_off"):
            return translate_state(mode_state_label)

        return translate_state(mode_name)

    @property
    def extra_state_attributes(self):
        detail = self.coordinator.data.get("detail", {})
        meta = self.coordinator.data.get("meta", {})

        return {
            "mode": detail.get("mode"),
            "mode_state": detail.get("modeState"),
            "mode_name": translate_state(detail.get("modeName")),
            "state_label": translate_state(detail.get("modeStateLabel")),
            "connected": meta.get("connected"),
            "activated": meta.get("activated"),
            "updated_date": detail.get("updatedDate"),
        }