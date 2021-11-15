"""Constant definitions for WeatherFlow Integration."""

DOMAIN = "weatherflow"

CONF_ADD_SENSORS = "add_sensors"
CONF_FORECAST_TYPE = "forecast_type"
CONF_INTERVAL_OBSERVATION = "interval_observation"
CONF_INTERVAL_FORECAST = "interval_forecast"
CONF_STATION_ID = "station_id"

CONFIG_OPTIONS = [
    CONF_INTERVAL_OBSERVATION,
    CONF_INTERVAL_FORECAST,
]

DEFAULT_ATTRIBUTION = "Powered by WeatherFlow"
DEFAULT_BRAND = "WeatherFlow"
DEFAULT_OBSERVATION_INTERVAL = 1
DEFAULT_FORECAST_INTERVAL = 30

FORECAST_TYPE_DAILY = "Daily"
FORECAST_TYPE_HOURLY = "Hourly"

WEATHERFLOW_PLATFORMS = [
    "binary_sensor",
    "sensor",
]

VALID_FORECAST_TYPES = [
    FORECAST_TYPE_DAILY,
    FORECAST_TYPE_HOURLY,
]
