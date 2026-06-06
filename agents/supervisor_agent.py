from agents.health_agent import (
    HealthAgent
)


class SupervisorAgent:

    def __init__(self):

        self.health_agent = (
            HealthAgent()
        )

    def route_health_query(
        self,
        profile,
        city,
        pm25,
        aqi_category
    ):

        return (
            self.health_agent
            .generate_advice(
                profile,
                city,
                pm25,
                aqi_category
            )
        )