"""Constant definitions for WeatherFlow Integration."""

from homeassistant.const import CONF_SCAN_INTERVAL

DOMAIN = "weatherflow"

CONF_INTERVAL_OBSERVATION = "interval_observation"
CONF_INTERVAL_FORECAST = "interval_forecast"
CONF_STATION_ID = "station_id"

CONFIG_OPTIONS = [
    CONF_SCAN_INTERVAL,
    CONF_INTERVAL_OBSERVATION,
    CONF_INTERVAL_FORECAST,
]

DEFAULT_ATTRIBUTION = "Powered by WeatherFlow"
DEFAULT_BRAND = "WeatherFlow"
DEFAULT_OBSERVATION_INTERVAL = 1
DEFAULT_FORECAST_INTERVAL = 30

WEATHERFLOW_PLATFORMS = [
    "sensor",
]
