"""
Karaca Connect Home Assistant Integration
Private local integration developed by AzadGLR.

Author: AzadGLR
Signature: by AzadGLR
Owner: AzadGLR
Version: 1.0.0
"""

from homeassistant.components.sensor import SensorEntity
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN, translate_state


async def async_setup_entry(hass, entry, async_add_entities):
    data = hass.data[DOMAIN][entry.entry_id]
    coordinator = data["coordinator"]

    async_add_entities(
        [
            KaracaStatusSensor(coordinator, entry),
        ]
    )


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
    """
    Tek durum sensörü.

    Bu sensör hem mod hem durum bilgisini tek yerde gösterir.
    Örnek çıktılar:
      - Kapalı
      - Su Kaynatma
      - Su Kaynatıyor
      - Su Kaynadı
      - Çay Demleme
      - Filtre Kahve
      - Mama Suyu
    """

    _attr_name = "Durum"
    _attr_unique_id = "karaca_cayci_durum"

    @property
    def native_value(self):
        detail = self.coordinator.data.get("detail", {})

        mode = detail.get("mode")
        mode_name = detail.get("modeName")
        mode_state_label = detail.get("modeStateLabel")

        # Cihaz standby ise direkt kapalı göster
        if str(mode) == "1":
            return "Kapalı"

        # API bazen modeStateLabel bilgisini geç güncelliyor.
        # Bu durumda modeName üzerinden hızlı durum gösteriyoruz.
        if mode_state_label in (None, "", "off", "standby_off"):
            return translate_state(mode_name)

        # API güncel durum döndürdüyse onu Türkçeleştir.
        return translate_state(mode_state_label)

    @property
    def extra_state_attributes(self):
        detail = self.coordinator.data.get("detail", {})
        meta = self.coordinator.data.get("meta", {})
        step_view = detail.get("stepView") or {}

        return {
            "author": "AzadGLR",
            "signature": "by AzadGLR",

            # Ham cihaz verileri
            "mode": detail.get("mode"),
            "mode_state": detail.get("modeState"),
            "raw_mode_name": detail.get("modeName"),
            "raw_mode_state_label": detail.get("modeStateLabel"),

            # Türkçeleştirilmiş değerler
            "mode_name": translate_state(detail.get("modeName")),
            "state_label": translate_state(detail.get("modeStateLabel")),

            # Step bilgisi
            "step_id": step_view.get("id"),
            "step_label": step_view.get("label"),

            # Bağlantı/metaveri
            "connected": meta.get("connected"),
            "activated": meta.get("activated"),
            "updated_date": detail.get("updatedDate"),
        }