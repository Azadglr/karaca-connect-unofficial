"""Karaca Connect Unofficial constants."""

DOMAIN = "karaca_connect"
INTEGRATION_NAME = "Karaca Connect Unofficial"
AUTHOR = "AzadGLR"
VERSION = "1.0.3"

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

# Bildirim / ses ayar switchleri switch.py içinde kullanılıyor.
SETTING_TEA_NOTIFICATION = 1
SETTING_FILTER_COFFEE_NOTIFICATION = 2
SETTING_FRESHNESS = 3
SETTING_POWER_OFF = 4
SETTING_NO_WATER = 5
SETTING_REMINDERS = 6
SETTING_VOICE = 7
SETTING_CLEANING = 8


MODE_TR = {
    # Kapalı / bekleme
    "standby": "Kapalı",
    "off": "Kapalı",
    "standbyoff": "Kapalı",
    "standby_off": "Kapalı",
    "poweroff": "Kapalı",
    "power_off": "Kapalı",

    # Su kaynatma
    "waterboiling": "Su kaynatılıyor",
    "water_boiling": "Su kaynatılıyor",
    "boilingwater": "Su kaynatılıyor",
    "boiling_water": "Su kaynatılıyor",
    "boiling": "Kaynatılıyor",
    "waterboiled": "Su Kaynadı",
    "water_boiled": "Su Kaynadı",
    "boiledwater": "Su Kaynadı",
    "boiled_water": "Su Kaynadı",
    "boiled": "Kaynadı",

    # Çay demleme
    "brewing": "Çay demleniyor",
    "teabrewing": "Çay demleniyor",
    "tea_brewing": "Çay demleniyor",

    # Çay hazır / taze
    "brewedfresh": "Çay taze",
    "brewed_fresh": "Çay taze",
    "fresh": "Taze",

    # Çay beklemiş / bayat
    "brewedstale": "Çay beklemiş",
    "brewed_stale": "Çay beklemiş",
    "stale": "Beklemiş",

    # Filtre kahve
    "filtercoffee": "Filtre kahve",
    "filter_coffee": "Filtre kahve",
    "coffeebrewing": "Kahve hazırlanıyor",
    "coffee_brewing": "Kahve hazırlanıyor",

    # Mama suyu
    "babyfood": "Mama suyu",
    "baby_food": "Mama suyu",
    "babywater": "Mama suyu",
    "baby_water": "Mama suyu",

    # Genel durumlar
    "ready": "Hazır",
    "completed": "Tamamlandı",
    "complete": "Tamamlandı",
    "done": "Tamamlandı",
    "working": "Çalışıyor",
    "running": "Çalışıyor",
    "active": "Aktif",
    "inactive": "Pasif",
    "idle": "Beklemede",
    "waiting": "Beklemede",

    # Hata / uyarı
    "error": "Hata",
    "fault": "Arıza",
    "nowater": "Su yok",
    "no_water": "Su yok",
    "lowwater": "Su az",
    "low_water": "Su az",
}


def translate_state(value):
    """Karaca API'den gelen İngilizce durumları Türkçeye çevirir."""
    if value is None:
        return None

    text = str(value).strip()

    if not text:
        return text

    key = (
        text
        .lower()
        .strip()
        .replace(" ", "")
        .replace("-", "_")
    )

    # Önce direkt dene
    if key in MODE_TR:
        return MODE_TR[key]

    # Sonra alt çizgisiz varyasyonu dene
    key_without_underscore = key.replace("_", "")
    if key_without_underscore in MODE_TR:
        return MODE_TR[key_without_underscore]

    # Bilinmeyen yeni bir API değeri gelirse ham değeri bozma.
    return text