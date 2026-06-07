from forecasting.forecast_tool import(
    get_pm25_forecast
)

from langchain_ollama import ChatOllama

class ForecastAgent:

    def __init__(self):
        self.llm = ChatOllama(
            model="llama3",
            temperature=0
        )

    def generate_forecast(
            self,
            city,
            query
    ):
        
        (
            historical_df,
            forecast_df,

            _
        ) = get_pm25_forecast(
            city=city,
            days=7
        )

        forecast_value = (
            forecast_df
            .tail(24)["yhat"]
            .mean()
        )

        prompt = f"""
        User Question:
        {query}

        City:
        {city}

        Predicted PM2.5:
        {forecast_value:.2f}

        Explain:
        - Forecast outlook
        - Pollution trend
        - Activity advice
        """

        response = (
            self.llm.invoke(prompt)
        )

        return response.content
