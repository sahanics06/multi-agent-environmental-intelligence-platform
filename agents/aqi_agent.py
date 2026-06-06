import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)

from langchain_ollama import ChatOllama
from tools.aqi_tool import get_air_quality
from utils.constants import AVAILABLE_CITIES

from forecasting.forecast_tool import (
    get_pm25_forecast
)

from utils.intents import (
    is_forecast_query
)

from agents.supervisor_agent import (
    SupervisorAgent
)

from utils.intents import (
    is_health_query
)

from agents.supervisor_agent import (
    SupervisorAgent
)

class AQIAgent:

    def __init__(self):

        self.llm = ChatOllama(
            model="llama3",
            temperature=0
        )
        self.supervisor = (
            SupervisorAgent()
        )

    def extract_city(
        self,
        query,
        chat_history=None
    ):

        """
        Extract city from current
        query or chat history
        """

        if not query:
            return None

        query_lower = str(query).lower()

        # First: search in current query
        for city in AVAILABLE_CITIES:

            if city.lower() in query_lower:
                return city

        # Second:
        # fallback to chat history
        if chat_history:

            for message in reversed(
                chat_history
            ):

                content = message.get(
                    "content",
                    ""
                ).lower()

                for city in (
                    AVAILABLE_CITIES
                ):

                    if (
                        city.lower()
                        in content
                    ):
                        return city

        return None

    def generate_response(
        self,
        query,
        chat_history=None
    ):

        if (
            not query
            or
            not str(query).strip()
        ):

            return (
                "Please ask a question."
            )

        city = self.extract_city(
                query,
                chat_history
            )

        if city is None:

            return (
                "Please mention a city.\n\n"
                f"Supported cities:\n"
                f"{', '.join(AVAILABLE_CITIES)}"
            )

        if is_forecast_query(query):

            (
                historical_df,
                forecast_df,
                _
            ) = get_pm25_forecast(
                city=city,
                days=7
            )

            forecast_value = (
                forecast_df.tail(24)["yhat"]
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

            1. AQI forecast
            2. Outdoor activity advice
            3. Health implications
            """

            response = self.llm.invoke(
                prompt
            )

            return response.content


        data = get_air_quality(city)

        if data is None:

            return (
                f"Could not fetch AQI "
                f"data for {city}."
            )

        row = data.iloc[0]

        if is_health_query(query):

            profile = "general"

            q = query.lower()

            if "asthma" in q:
                profile = "asthma"

            elif (
                "child" in q
                or
                "children" in q
            ):
                profile = "child"

            elif "elderly" in q:
                profile = "elderly"

            return (
                self.supervisor
                .route_health_query(
                    profile=profile,
                    city=city,
                    pm25=row["pm2_5"],
                    aqi_category=row[
                        "aqi_category"
                    ]
                )
            )

        prompt = f"""
        You are an expert
        environmental AI assistant.

        User question:
        {query}

        Previous conversation:
        {chat_history}

        Air quality data:

        City: {city}
        PM2.5: {row['pm2_5']}
        PM10: {row['pm10']}
        NO2:
        {row['nitrogen_dioxide']}
        CO:
        {row['carbon_monoxide']}
        Ozone:
        {row['ozone']}

        AQI Category:
        {row['aqi_category']}

        Rules:
        - Answer naturally
        - Understand context
        - Give activity advice
        - Mention AQI status
        - Keep concise
        """

        response = (
            self.llm.invoke(
                prompt
            )
        )

        return response.content