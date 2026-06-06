FORECAST_KEYWORDS = [
    "forecast",
    "predict",
    "prediction",
    "tomorrow",
    "future",
    "next week",
    "weekend",
    "coming days"
]


HEALTH_KEYWORDS = [
    "asthma",
    "child",
    "children",
    "elderly",
    "health",
    "safe",
    "jog",
    "exercise",
    "run",
    "cycling"
]


def is_health_query(query):

    query = query.lower()

    return any(
        keyword in query
        for keyword in HEALTH_KEYWORDS
    )

def is_forecast_query(query):

    query = query.lower()

    return any(
        keyword in query
        for keyword in FORECAST_KEYWORDS
    )