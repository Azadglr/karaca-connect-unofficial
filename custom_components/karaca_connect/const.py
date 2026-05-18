"""Karaca Connect Unofficial constants."""

DOMAIN = "karaca_connect"

INTEGRATION_NAME = "Karaca Connect Unofficial"
AUTHOR = "AzadGLR"
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

ACTIVE_MODE_IDS = {
    MODE_FILTER_COFFEE,
    MODE_BOILING_WATER,
    MODE_TEA_BREWING,
    MODE_BABY_FOOD,
}

MODE_TR = {
    "standby": "Kapalı",
    "off": "Kapalı",
    "standbyoff": "Kapalı",

    "boilingwater": "Su Kaynatma",
    "waterboiling": "Su Kaynıyor",
    "waterboiled": "Su Kaynadı",
    "waterready": "Su Kaynadı",
    "suhazir": "Su Kaynadı",
    "hazir": "Su Kaynadı",

    "teabrewing": "Çay Demleme",
    "brewing": "Çay Demleniyor",
    "brewedfresh": "Taze Çay",
    "brewedstale": "Bayat Çay",

    "filtercoffee": "Filtre Kahve",
    "babyfood": "Mama Suyu",

    "finished": "Tamamlandı",
    "completed": "Tamamlandı",
    "ready": "Hazır",
    "error": "Hata",
}


def translate_state(value):
    if value is None:
        return None

    key = str(value).replace("_", "").replace("-", "").replace(" ", "").lower()
    return MODE_TR.get(key, value)