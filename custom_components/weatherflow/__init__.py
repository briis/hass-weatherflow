"""WeatherFlow Platform."""
from __future__ import annotations

import logging

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import (
    CONF_API_TOKEN,
    CONF_ID,
    EVENT_HOMEASSISTANT_STOP,
)
from homeassistant.core import HomeAssistant, callback
from homeassistant.exceptions import ConfigEntryNotReady
from homeassistant.helpers.aiohttp_client import async_create_clientsession
import homeassistant.helpers.device_registry as dr

from pyweatherflowrest import (
    WrongStationID,
    NotAuthorized,
    BadRequest,
    Invalid,
    WeatherFlowApiClient,
)
from .const import (
    DOMAIN,
    CONF_INTERVAL_OBSERVATION,
    CONF_INTERVAL_FORECAST,
    CONF_STATION_ID,
)

_LOGGER = logging.getLogger(__name__)
