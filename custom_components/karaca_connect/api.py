"""Karaca Connect Unofficial API client."""

from aiohttp import ClientSession

from .const import BASE_URL, VERSION


def _extract_api_message(data):
    if not isinstance(data, dict):
        return str(data)
    messages = data.get("messages")
    if isinstance(messages, list) and messages:
        return " ".join(str(message) for message in messages)
    if isinstance(messages, str) and messages:
        return messages
    return str(data.get("raw") or data)


class KaracaConnectApi:
    def __init__(self, session: ClientSession, email: str, password: str, device_id: str | None = None):
        self.session = session
        self.email = email
        self.password = password
        self.device_id = str(device_id) if device_id else None
        self.token = None

    async def _request(self, method: str, path: str, *, json_data=None, auth=True):
        url = f"{BASE_URL}{path}"
        headers = {
            "Content-Type": "application/json",
            "User-Agent": f"HomeAssistant-KaracaConnect-Unofficial/{VERSION}",
        }
        if auth:
            if not self.token:
                await self.login()
            headers["Authorization"] = f"Bearer {self.token}"
        async with self.session.request(method, url, headers=headers, json=json_data, timeout=20) as resp:
            text = await resp.text()
            try:
                data = await resp.json()
            except Exception:
                data = {"raw": text}
            if resp.status == 401 and auth:
                self.token = None
                await self.login()
                headers["Authorization"] = f"Bearer {self.token}"
                async with self.session.request(method, url, headers=headers, json=json_data, timeout=20) as retry_resp:
                    retry_text = await retry_resp.text()
                    try:
                        retry_data = await retry_resp.json()
                    except Exception:
                        retry_data = {"raw": retry_text}
                    return retry_resp.status, retry_data
            return resp.status, data

    async def login(self):
        status, data = await self._request(
            "POST",
            "/api/auth/signin",
            json_data={"email": self.email, "password": self.password},
            auth=False,
        )
        if status != 200 or data.get("succeeded") is False:
            raise RuntimeError(f"Karaca login failed: {_extract_api_message(data)}")
        token = data.get("data", {}).get("jwToken")
        if not token:
            raise RuntimeError("Karaca token not found")
        self.token = token
        return token

    async def get_devices(self):
        status, data = await self._request("GET", "/api/v1/devices/me")
        if status != 200 or data.get("succeeded") is False:
            raise RuntimeError(f"Device list failed: {_extract_api_message(data)}")
        return data.get("data", [])

    async def resolve_device_id(self):
        if self.device_id:
            return self.device_id
        devices = await self.get_devices()
        if not devices:
            raise RuntimeError("No Karaca devices found")
        self.device_id = str(devices[0].get("id"))
        return self.device_id

    async def get_detail(self):
        device_id = await self.resolve_device_id()
        status, data = await self._request("GET", f"/api/v1/devices/{device_id}")
        if status != 200 or data.get("succeeded") is False:
            raise RuntimeError(f"Device detail failed: {_extract_api_message(data)}")
        return data.get("data", {})

    async def get_settings(self):
        device_id = await self.resolve_device_id()
        status, data = await self._request("GET", f"/api/v1/devices/{device_id}/settings")
        if status != 200 or data.get("succeeded") is False:
            raise RuntimeError(f"Settings failed: {_extract_api_message(data)}")
        return data.get("data", {}).get("notifications", [])

    async def set_mode(self, mode_id: int, active: bool = True):
        device_id = await self.resolve_device_id()
        status, data = await self._request(
            "PUT",
            f"/api/v1/devices/{device_id}/modes/{mode_id}",
            json_data={"active": active},
        )
        if status != 200 or data.get("succeeded") is False:
            raise RuntimeError(_extract_api_message(data))
        return data

    async def set_setting(self, setting_id: int, value: bool):
        device_id = await self.resolve_device_id()
        status, data = await self._request(
            "PUT",
            f"/api/v1/devices/{device_id}/settings/{setting_id}",
            json_data={"value": value},
        )
        if status == 200 and data.get("succeeded") is not False:
            return data
        status2, data2 = await self._request(
            "PUT",
            f"/api/v1/devices/{device_id}/settings/{setting_id}",
            json_data={"active": value},
        )
        if status2 != 200 or data2.get("succeeded") is False:
            raise RuntimeError(f"Set setting failed: {_extract_api_message(data2)}")
        return data2
