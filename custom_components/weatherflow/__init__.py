"""WeatherFlow Platform."""
from __future__ import annotations

import logging
from datetime import timedelta

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import (
    CONF_API_TOKEN,
    CONF_ID,
    CONF_SCAN_INTERVAL,
)
from homeassistant.core import HomeAssistant, callback
from homeassistant.exceptions import ConfigEntryNotReady
from homeassistant.helpers.aiohttp_client import async_create_clientsession
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator
import homeassistant.helpers.device_registry as dr

from pyweatherflowrest import (
    WrongStationID,
    NotAuthorized,
    BadRequest,
    Invalid,
    WeatherFlowApiClient,
)
from pyweatherflowrest.data import StationDescription
from .const import (
    DOMAIN,
    CONFIG_OPTIONS,
    CONF_STATION_ID,
    DEFAULT_BRAND,
    DEFAULT_OBSERVATION_INTERVAL,
    WEATHERFLOW_PLATFORMS,
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

    session = async_create_clientsession(hass)

    weatherflowapi = WeatherFlowApiClient(
        entry.data[CONF_STATION_ID], entry.data[CONF_API_TOKEN], session=session
    )

    try:
        await weatherflowapi.initialize()
        station_data: StationDescription = weatherflowapi.station_data

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

    if entry.unique_id is None:
        hass.config_entries.async_update_entry(
            entry, unique_id=station_data.hub_serial_number
        )

    coordinator = DataUpdateCoordinator(
        hass,
        _LOGGER,
        name=DOMAIN,
        update_method=weatherflowapi.update_observations,
        update_interval=timedelta(
            minutes=entry.options.get(CONF_SCAN_INTERVAL, DEFAULT_OBSERVATION_INTERVAL)
        ),
    )
    await coordinator.async_refresh()
    if not coordinator.last_update_success:
        raise ConfigEntryNotReady

    hass.data.setdefault(DOMAIN, {})[entry.entry_id] = {
        "coordinator": coordinator,
        "weatherflowapi": weatherflowapi,
        "station_data": station_data,
    }

    await _async_get_or_create_nvr_device_in_registry(hass, entry, station_data)

    hass.config_entries.async_setup_platforms(entry, WEATHERFLOW_PLATFORMS)

    entry.async_on_unload(entry.add_update_listener(_async_options_updated))

    return True


async def _async_get_or_create_nvr_device_in_registry(
    hass: HomeAssistant, entry: ConfigEntry, station_data: StationDescription
) -> None:
    device_registry = await dr.async_get_registry(hass)
    _model = "AIR & SKY"
    if station_data.is_tempest:
        _model = "Tempest"
    device_registry.async_get_or_create(
        config_entry_id=entry.entry_id,
        connections={(dr.CONNECTION_NETWORK_MAC, station_data.hub_serial_number)},
        identifiers={(DOMAIN, station_data.hub_serial_number)},
        manufacturer=DEFAULT_BRAND,
        name=entry.data[CONF_ID],
        model=_model,
        sw_version=station_data.hub_firmware_revision,
    )


async def _async_options_updated(hass: HomeAssistant, entry: ConfigEntry):
    """Update options."""
    await hass.config_entries.async_reload(entry.entry_id)


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload Unifi Protect config entry."""
    unload_ok = await hass.config_entries.async_unload_platforms(
        entry, WEATHERFLOW_PLATFORMS
    )

    if unload_ok:
        data = hass.data[DOMAIN][entry.entry_id]
        await data["weatherflowapi"].req.close()
        hass.data[DOMAIN].pop(entry.entry_id)

    return unload_ok
