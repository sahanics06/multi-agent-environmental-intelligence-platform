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


class AQIAgent:

    def __init__(self):

        self.llm = ChatOllama(
            model="llama3",
            temperature=0
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

        data = get_air_quality(city)

        if data is None:

            return (
                f"Could not fetch AQI "
                f"data for {city}."
            )

        row = data.iloc[0]

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