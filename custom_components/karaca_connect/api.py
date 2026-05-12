"""
Karaca Connect Home Assistant Integration
Private local integration developed by AzadGLR.

Author: AzadGLR
Signature: by AzadGLR
Owner: AzadGLR
Version: 1.0.0
"""

from aiohttp import ClientSession

from .const import BASE_URL, AUTHOR, VERSION, MODE_STANDBY


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

        async with self.session.request(
            method,
            url,
            headers=headers,
            json=json_data,
            timeout=20,
        ) as resp:
            text = await resp.text()

            try:
                data = await resp.json()
            except Exception:
                data = {"raw": text}

            if resp.status == 401 and auth:
                self.token = None
                await self.login()
                headers["Authorization"] = f"Bearer {self.token}"

                async with self.session.request(
                    method,
                    url,
                    headers=headers,
                    json=json_data,
                    timeout=20,
                ) as retry_resp:
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
            json_data={
                "email": self.email,
                "password": self.password,
            },
            auth=False,
        )

        if status != 200:
            raise RuntimeError(f"Karaca login failed: {status} {data}")

        token = data.get("data", {}).get("jwToken")

        if not token:
            raise RuntimeError("Karaca token not found")

        self.token = token
        return token

    async def get_devices(self):
        status, data = await self._request("GET", "/api/v1/devices/me")

        if status != 200:
            raise RuntimeError(f"Device list failed: {status} {data}")

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

        status, data = await self._request(
            "GET",
            f"/api/v1/devices/{device_id}",
        )

        if status != 200:
            raise RuntimeError(f"Device detail failed: {status} {data}")

        return data.get("data", {})

    async def get_settings(self):
        device_id = await self.resolve_device_id()

        status, data = await self._request(
            "GET",
            f"/api/v1/devices/{device_id}/settings",
        )

        if status != 200:
            raise RuntimeError(f"Settings failed: {status} {data}")

        return data.get("data", {}).get("notifications", [])

    async def set_mode(self, mode_id: int, active: bool = True):
        device_id = await self.resolve_device_id()

        status, data = await self._request(
            "PUT",
            f"/api/v1/devices/{device_id}/modes/{mode_id}",
            json_data={"active": active},
        )

        if status != 200:
            raise RuntimeError(f"Set mode failed: {status} {data}")

        return data

    async def standby(self):
        return await self.set_mode(MODE_STANDBY, True)

    async def toggle_mode(self, mode_id: int):
        detail = await self.get_detail()
        current_mode = detail.get("detail", {}).get("mode")

        if str(current_mode) == str(mode_id):
            return await self.standby()

        return await self.set_mode(mode_id, True)

    async def set_setting(self, setting_id: int, value: bool):
        device_id = await self.resolve_device_id()

        status, data = await self._request(
            "PUT",
            f"/api/v1/devices/{device_id}/settings/{setting_id}",
            json_data={"value": value},
        )

        if status == 200:
            return data

        status2, data2 = await self._request(
            "PUT",
            f"/api/v1/devices/{device_id}/settings/{setting_id}",
            json_data={"active": value},
        )

        if status2 != 200:
            raise RuntimeError(f"Set setting failed: {status2} {data2}")

        return data2