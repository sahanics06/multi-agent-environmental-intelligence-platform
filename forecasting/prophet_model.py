import pandas as pd
from prophet import Prophet
import plotly.graph_objects as go


class AQIForecaster:

    def __init__(self):

        self.model = Prophet(
        daily_seasonality=True,
        weekly_seasonality=True,
        yearly_seasonality=False
    )

    def prepare_data(
        self,
        file_path,
        target_column="pm2_5"
    ):

        """
        Prepare dataset for Prophet
        """

        df = pd.read_csv(file_path)

        df["timestamp"] = pd.to_datetime(
            df["timestamp"]
        )

        prophet_df = df[
            ["timestamp", target_column]
        ].copy()

        prophet_df.columns = [
            "ds",
            "y"
        ]

        prophet_df = (
            prophet_df
            .dropna()
        )

        return prophet_df

    def train_model(
        self,
        df
    ):

        """
        Train Prophet model
        """

        self.model.fit(df)

    def forecast(
        self,
        periods=7
    ):

        """
        Forecast future AQI
        """

        future = (
            self.model
            .make_future_dataframe(
                periods=periods * 24,
                freq="h"
            )
        )

        forecast_df = (
            self.model.predict(
                future
            )
        )

        return forecast_df

    def create_forecast_chart(
        self,
        historical_df,
        forecast_df
    ):

        fig = go.Figure()

        # Historical data
        fig.add_trace(
            go.Scatter(
                x=historical_df["ds"],
                y=historical_df["y"],
                mode="lines",
                name="Historical AQI"
            )
        )

        # Forecast
        fig.add_trace(
            go.Scatter(
                x=forecast_df["ds"],
                y=forecast_df["yhat"],
                mode="lines",
                name="Forecast"
            )
        )

        fig.update_layout(
            title=(
                "PM2.5 Forecast"
            ),
            xaxis_title="Date",
            yaxis_title="PM2.5"
        )

        return fig


if __name__ == "__main__":

    forecaster = AQIForecaster()

    df = forecaster.prepare_data(
        "data/pune_aqi.csv"
    )

    forecaster.train_model(df)

    forecast = (
        forecaster.forecast(
            periods=7
        )
    )

    print(
        forecast[
            ["ds", "yhat"]
        ].tail()
    )