from forecasting.prophet_model import AQIForecaster


def get_pm25_forecast(
    city="Pune",
    days=7
):

    file_path = (
        f"data/{city.lower()}_aqi.csv"
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