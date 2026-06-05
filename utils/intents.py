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


def is_forecast_query(query):

    query = query.lower()

    return any(
        keyword in query
        for keyword in FORECAST_KEYWORDS
    )