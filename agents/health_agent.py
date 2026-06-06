from langchain_ollama import ChatOllama


class HealthAgent:

    def __init__(self):

        self.llm = ChatOllama(
            model="llama3",
            temperature=0
        )

    def generate_advice(
        self,
        profile,
        city,
        pm25,
        aqi_category
    ):

        prompt = f"""
        You are an environmental
        health advisor.

        User Profile:
        {profile}

        City:
        {city}

        PM2.5:
        {pm25}

        AQI Category:
        {aqi_category}

        Provide:

        1. Risk level
        2. Outdoor activity advice
        3. Precautions

        Keep answer concise.
        """

        response = self.llm.invoke(
            prompt
        )

        return response.content