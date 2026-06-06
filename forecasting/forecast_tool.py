from forecasting.prophet_model import (
    AQIForecaster
)

import os

from forecasting.data_collector import (
    collect_historical_aqi
)


def get_pm25_forecast(
    city="Pune",
    days=7
):

    file_path = (
        f"data/{city.lower()}_aqi.csv"
    )

    # Auto-create dataset
    if not os.path.exists(
        file_path
    ):

        df = (
            collect_historical_aqi(
                city=city,
                days=90
            )
        )

        if df is None:

            raise Exception(
                f"Could not collect "
                f"historical data for {city}"
            )

        os.makedirs(
            "data",
            exist_ok=True
        )

        df.to_csv(
            file_path,
            index=False
        )

    forecaster = AQIForecaster()

    historical_df = (
        forecaster.prepare_data(
            file_path
        )
    )

    forecaster.train_model(
        historical_df
    )

    forecast_df = (
        forecaster.forecast(
            periods=days
        )
    )

    return (
        historical_df,
        forecast_df,
        forecaster
    )