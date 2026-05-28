import requests
import pandas as pd


GEOCODING_BASE_URL = (
    "https://geocoding-api.open-meteo.com/v1/search"
)

AIR_QUALITY_BASE_URL = (
    "https://air-quality-api.open-meteo.com/v1/air-quality"
)


def get_city_coordinates(city: str):

    url = (
        f"{GEOCODING_BASE_URL}"
        f"?name={city}&count=1"
    )

    response = requests.get(url)

    if response.status_code != 200:
        return None

    data = response.json()

    if "results" not in data:
        return None

    result = data["results"][0]

    return {
        "city": result["name"],
        "latitude": result["latitude"],
        "longitude": result["longitude"]
    }


def classify_aqi(pm25: float):

    """
    AQI classification based on PM2.5
    """

    if pm25 is None:
        return "Unknown", "⚪"

    if pm25 <= 12:
        return "Good", "🟢"

    elif pm25 <= 35:
        return "Moderate", "🟡"

    elif pm25 <= 55:
        return (
            "Unhealthy for Sensitive Groups",
            "🟠"
        )

    elif pm25 <= 150:
        return "Unhealthy", "🔴"

    elif pm25 <= 250:
        return "Very Unhealthy", "🟣"

    return "Hazardous", "⚫"


def get_air_quality(city: str):

    """
    Fetch real-time air quality data
    """

    location = get_city_coordinates(city)

    if not location:
        return None

    latitude = location["latitude"]
    longitude = location["longitude"]

    url = (
        f"{AIR_QUALITY_BASE_URL}"
        f"?latitude={latitude}"
        f"&longitude={longitude}"
        "&current="
        "pm10,"
        "pm2_5,"
        "carbon_monoxide,"
        "nitrogen_dioxide,"
        "sulphur_dioxide,"
        "ozone"
    )

    response = requests.get(url)

    if response.status_code != 200:
        return None

    data = response.json()

    current = data.get("current", {})

    pm25 = current.get("pm2_5")

    category, indicator = classify_aqi(pm25)

    result = {
        "city": city,
        "pm2_5": current.get("pm2_5"),
        "pm10": current.get("pm10"),
        "carbon_monoxide": current.get(
            "carbon_monoxide"
        ),
        "nitrogen_dioxide": current.get(
            "nitrogen_dioxide"
        ),
        "sulphur_dioxide": current.get(
            "sulphur_dioxide"
        ),
        "ozone": current.get("ozone"),
        "aqi_category": category,
        "indicator": indicator
    }

    return pd.DataFrame([result])