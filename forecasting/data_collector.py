import requests
import pandas as pd
from datetime import datetime
import os
import sys
sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)

from tools.aqi_tool import(
    get_city_coordinates
)

def collect_historical_aqi(
        city,
        days=90
):
    
    """
    Collect historical AQI data 
    using Open-Meteo API
    """

    location = (
        get_city_coordinates(city)
    )

    if not location:
        print(
            f"Could not find{city}"
        )
        return None
    
    latitude = (
        location["latitude"]
    )

    longitude = (
        location["longitude"]
    )

    end_date = (
        datetime.today()
    )

    start_date = (
        end_date - pd.Timedelta(days=days)
    )

    url = (
        "https://air-quality-api.open-meteo.com/v1/air-quality"
        f"?latitude={latitude}"
        f"&longitude={longitude}"
        f"&start_date="
        f"{start_date.date()}"
        f"&end_date="
        f"{end_date.date()}"
        "&hourly="
        "pm2_5,"
        "pm10,"
        "nitrogen_dioxide,"
        "sulphur_dioxide,"
        "ozone,"
        "carbon_monoxide"
    )

    response = requests.get(url)

    if response.status_code != 200:
        print("Failed to fetch data")
        return None
    
    data = response.json()

    hourly = (
        data.get(
            "hourly", {}
        )
    )

    df = pd.DataFrame({
        "timestamp":
        hourly.get("time", []),

        "pm2_5":
        hourly.get("pm2_5", []),

        "pm10":
        hourly.get("pm10", []),

        "nitrogen_dioxide":
        hourly.get(
            "nitrogen_dioxide",
            []
        ),

        "sulphur_dioxide":
        hourly.get(
            "sulphur_dioxide",
            []
        ),

        "ozone":
        hourly.get(
            "ozone",
            []
        ),

        "carbon_monoxide":
        hourly.get(
            "carbon_monoxide",
            []
        )
    })

    df["city"] = city

    return df


if __name__=="__main__":

    city = "Pune"

    df = collect_historical_aqi(
        city=city,
        days=90
    )

    if df is not None:

        os.makedirs(
            "data",
            exist_ok=True
        )

        file_path = (
            f"data/"
            f"{city.lower()}_aqi.csv"
        )

        df.to_csv(
            file_path,
            index=False
        )

        print(
            f"Saved to "
            f"{file_path}"
        )

        print(df.head())