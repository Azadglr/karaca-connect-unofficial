"""Karaca Connect Unofficial config flow."""

import logging

import voluptuous as vol

from homeassistant import config_entries
from homeassistant.helpers.aiohttp_client import async_get_clientsession

from .api import KaracaConnectApi
from .const import CONF_DEVICE_ID, CONF_EMAIL, CONF_PASSWORD, DOMAIN

_LOGGER = logging.getLogger(__name__)


class KaracaConnectConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1

    def __init__(self):
        self._email = None
        self._password = None
        self._devices = []

    async def async_step_user(self, user_input=None):
        errors = {}

        if user_input is not None:
            self._email = user_input[CONF_EMAIL]
            self._password = user_input[CONF_PASSWORD]

            try:
                session = async_get_clientsession(self.hass)
                api = KaracaConnectApi(session, self._email, self._password)

                await api.login()
                self._devices = await api.get_devices()

                if not self._devices:
                    errors["base"] = "no_devices"
                elif len(self._devices) == 1:
                    return await self._create_entry_for_device(self._devices[0])
                else:
                    return await self.async_step_select_device()

            except Exception as err:
                _LOGGER.exception("Karaca Connect setup failed: %s", err)
                errors["base"] = "cannot_connect"

        schema = vol.Schema(
            {
                vol.Required(CONF_EMAIL): str,
                vol.Required(CONF_PASSWORD): str,
            }
        )

        return self.async_show_form(
            step_id="user",
            data_schema=schema,
            errors=errors,
        )

    async def async_step_select_device(self, user_input=None):
        errors = {}

        device_options = {
            str(device.get("id")): f"{device.get('label') or 'Karaca Cihaz'} ({device.get('type') or 'unknown'})"
            for device in self._devices
        }

        if user_input is not None:
            selected_device_id = user_input[CONF_DEVICE_ID]
            selected_device = next(
                (
                    device
                    for device in self._devices
                    if str(device.get("id")) == str(selected_device_id)
                ),
                None,
            )

            if selected_device:
                return await self._create_entry_for_device(selected_device)

            errors["base"] = "device_not_found"

        schema = vol.Schema(
            {
                vol.Required(CONF_DEVICE_ID): vol.In(device_options),
            }
        )

        return self.async_show_form(
            step_id="select_device",
            data_schema=schema,
            errors=errors,
        )

    async def _create_entry_for_device(self, device):
        device_id = str(device.get("id"))
        label = device.get("label") or "Karaca Çaycı"

        await self.async_set_unique_id(f"karaca_{device_id}")
        self._abort_if_unique_id_configured()

        return self.async_create_entry(
            title=label,
            data={
                CONF_EMAIL: self._email,
                CONF_PASSWORD: self._password,
                CONF_DEVICE_ID: device_id,
            },
        )