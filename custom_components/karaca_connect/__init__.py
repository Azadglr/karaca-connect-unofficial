"""
Karaca Connect Home Assistant Integration
Private local integration developed by AzadGLR.

Author: AzadGLR
Signature: by AzadGLR
Owner: AzadGLR
Version: 1.0.0
"""

import logging
from datetime import timedelta

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator

from .api import KaracaConnectApi
from .const import (
    DOMAIN,
    PLATFORMS,
    CONF_EMAIL,
    CONF_PASSWORD,
    CONF_DEVICE_ID,
)

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    session = async_get_clientsession(hass)

    api = KaracaConnectApi(
        session=session,
        email=entry.data[CONF_EMAIL],
        password=entry.data[CONF_PASSWORD],
        device_id=entry.data.get(CONF_DEVICE_ID),
    )

    async def async_update_data():
        return await api.get_detail()

    coordinator = DataUpdateCoordinator(
        hass,
        _LOGGER,
        name="Karaca Connect Unofficial",
        update_method=async_update_data,
        update_interval=timedelta(seconds=20),
    )

    await api.login()
    await api.resolve_device_id()
    await coordinator.async_config_entry_first_refresh()

    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN][entry.entry_id] = {
        "api": api,
        "coordinator": coordinator,
    }

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    unload_ok = await hass.config_entries.async_unload_platforms(entry, PLATFORMS)

    if unload_ok:
        hass.data[DOMAIN].pop(entry.entry_id)

    return unload_ok