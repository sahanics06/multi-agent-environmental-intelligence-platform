from agents.health_agent import (
    HealthAgent
)

from agents.forecast_agent import(
    ForecastAgent
)

from utils.intents import(
    is_forecast_query,
    is_health_query
)


class SupervisorAgent:

    def __init__(self):

        self.health_agent = (
            HealthAgent()
        )

        self.forecast_agent = (
            ForecastAgent()
        )

    def handle_query(
        self,
        query,
        city,
        pm25,
        aqi_category
    ):
        forecast_answer = None
        health_answer = None

        if is_forecast_query(
            query
        ):
            forecast_answer = (
                self.forecast_agent
                .generate_forecast(
                    city,
                    query
                )
            )

        if is_health_query(
            query
        ):
            profile = "general"

            q = query.lower()

            if "asthma" in q:
                profile = "asthma"

            elif ("child" in q or "children" in q):
                profile = "child"

            elif "elderly" in q:
                profile = "elderly"

            health_answer = (
                self.health_agent
                .generate_advice(
                    profile,
                    city,
                    pm25,
                    aqi_category
                )
            )


        return (
            forecast_answer,
            health_answer
        )