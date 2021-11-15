"""Constant definitions for WeatherFlow Integration."""

DOMAIN = "weatherflow"

CONDITION_CLASSES = {
    "clear-night": ["clear-night"],
    "cloudy": ["cloudy"],
    "exceptional": ["cloudy"],
    "fog": ["foggy"],
    "hail": ["hail"],
    "lightning": ["thunderstorm"],
    "lightning-rainy": ["possibly-thunderstorm-day", "possibly-thunderstorm-night"],
    "partlycloudy": [
        "partly-cloudy-day",
        "partly-cloudy-night",
    ],
    "rainy": [
        "rainy",
        "possibly-rainy-day",
        "possibly-rainy-night",
    ],
    "snowy": ["snow", "possibly-snow-day", "possibly-snow-night"],
    "snowy-rainy": ["sleet", "possibly-sleet-day", "possibly-sleet-night"],
    "sunny": ["clear-day"],
    "windy": ["windy"],
}

CONF_INTERVAL_OBSERVATION = "interval_observation"
CONF_INTERVAL_FORECAST = "interval_forecast"
CONF_STATION_ID = "station_id"

CONFIG_OPTIONS = [
    CONF_INTERVAL_OBSERVATION,
    CONF_INTERVAL_FORECAST,
]

DEFAULT_ATTRIBUTION = "Powered by WeatherFlow"
DEFAULT_BRAND = "WeatherFlow"
DEFAULT_OBSERVATION_INTERVAL = 2
DEFAULT_FORECAST_INTERVAL = 30

WEATHERFLOW_PLATFORMS = [
    "binary_sensor",
    "sensor",
    "weather",
]
