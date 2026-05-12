"""
Karaca Connect Home Assistant Integration
Private local integration developed by AzadGLR.

Author: AzadGLR
Signature: by AzadGLR
Owner: AzadGLR
Version: 1.0.0
"""

DOMAIN = "karaca_connect"
INTEGRATION_NAME = "Karaca Connect Unofficial"
AUTHOR = "AzadGLR"
SIGNATURE = "Private build"
VERSION = "1.0.0"

BASE_URL = "https://karacaconnectapi.krc.com.tr"

CONF_EMAIL = "email"
CONF_PASSWORD = "password"
CONF_DEVICE_ID = "device_id"

PLATFORMS = ["sensor", "switch"]

MODE_STANDBY = 1
MODE_FILTER_COFFEE = 2
MODE_BOILING_WATER = 6
MODE_TEA_BREWING = 9
MODE_BABY_FOOD = 13

SETTING_TEA_NOTIFICATION = 1
SETTING_FILTER_COFFEE_NOTIFICATION = 2
SETTING_FRESHNESS = 3
SETTING_POWER_OFF = 4
SETTING_NO_WATER = 5
SETTING_REMINDERS = 6
SETTING_VOICE = 7
SETTING_CLEANING = 8


MODE_TR = {
    "standby": "Kapalı",
    "off": "Kapalı",
    "boilingwater": "Su Kaynatma",
    "waterboiling": "Su Kaynatıyor",
    "waterboiled": "Su Kaynadı",
    "teabrewing": "Çay Demleme",
    "filtercoffee": "Filtre Kahve",
    "babyfood": "Mama Suyu",
}


def translate_state(value):
    if value is None:
        return None

    key = str(value).replace("_", "").replace("-", "").lower()
    return MODE_TR.get(key, value)