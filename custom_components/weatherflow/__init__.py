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
    CONFIG_OPTIONS,
    CONF_STATION_ID,
)

_LOGGER = logging.getLogger(__name__)


@callback
def _async_import_options_from_data_if_missing(hass: HomeAssistant, entry: ConfigEntry):
    options = dict(entry.options)
    data = dict(entry.data)
    modified = False
    for importable_option in CONFIG_OPTIONS:
        if importable_option not in entry.options and importable_option in entry.data:
            options[importable_option] = entry.data[importable_option]
            del data[importable_option]
            modified = True

    if modified:
        hass.config_entries.async_update_entry(entry, data=data, options=options)


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up the WeatherFlow config entries."""
    _async_import_options_from_data_if_missing(hass, entry)

    weatherflow = WeatherFlowApiClient(
        entry.data[CONF_STATION_ID], entry.data[CONF_API_TOKEN]
    )

    try:
        await weatherflow.initialize()

    except WrongStationID:
        _LOGGER.debug("The Station Id entered is not correct")
        return False
    except Invalid as notreadyerror:
        _LOGGER.error("The data returned from WeatherFlow is invalid")
        raise ConfigEntryNotReady from notreadyerror
    except NotAuthorized:
        _LOGGER.debug("The Api Token entered is not correct")
        return False
    except BadRequest as notreadyerror:
        _LOGGER.error("An unknown error occurred when retreiving data")
        raise ConfigEntryNotReady from notreadyerror
