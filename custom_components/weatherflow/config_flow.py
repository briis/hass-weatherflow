"""Config Flow to configure WeatherFlow Integration."""
from __future__ import annotations
import logging

from homeassistant import config_entries
from homeassistant.const import CONF_API_TOKEN, CONF_ID
from homeassistant.core import callback
from homeassistant.helpers.aiohttp_client import async_create_clientsession

from pyweatherflowrest import (
    WrongStationID,
    NotAuthorized,
    BadRequest,
    Invalid,
    WeatherFlowApiClient,
)
from pyweatherflowrest.data import StationDescription
import voluptuous as vol

from .const import (
    DOMAIN,
    CONF_ADD_SENSORS,
    CONF_FORECAST_TYPE,
    CONF_INTERVAL_OBSERVATION,
    CONF_INTERVAL_FORECAST,
    CONF_STATION_ID,
    FORECAST_TYPE_DAILY,
    VALID_FORECAST_TYPES,
)

_LOGGER = logging.getLogger(__name__)


class WeatherFlowFlowHandler(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a WeatherFlow config flow."""

    VERSION = 1

    @staticmethod
    @callback
    def async_get_options_flow(config_entry):
        """Get the options flow for this handler."""
        return OptionsFlowHandler(config_entry)

    async def async_step_user(self, user_input=None):
        """Handle a flow initiated by the user."""
        if user_input is None:
            return await self._show_setup_form(user_input)

        errors = {}

        session = async_create_clientsession(self.hass)

        weatherflow = WeatherFlowApiClient(
            user_input[CONF_STATION_ID], user_input[CONF_API_TOKEN], session=session
        )

        try:
            await weatherflow.initialize()

            station_data: StationDescription = weatherflow.station_data

        except WrongStationID as err:
            _LOGGER.debug(err)
            errors["base"] = "wrong_station_id"
            return await self._show_setup_form(errors)
        except Invalid as err:
            _LOGGER.debug(err)
            errors["base"] = "invalid_data"
            return await self._show_setup_form(errors)
        except NotAuthorized as err:
            _LOGGER.debug(err)
            errors["base"] = "wrong_token"
            return await self._show_setup_form(errors)
        except BadRequest as err:
            _LOGGER.debug(err)
            errors["base"] = "bad_request"
            return await self._show_setup_form(errors)

        unique_id = station_data.hub_serial_number

        await self.async_set_unique_id(unique_id)
        self._abort_if_unique_id_configured()

        return self.async_create_entry(
            title=station_data.name,
            data={
                CONF_ID: station_data.name,
                CONF_STATION_ID: user_input[CONF_STATION_ID],
                CONF_API_TOKEN: user_input[CONF_API_TOKEN],
                CONF_FORECAST_TYPE: user_input[CONF_FORECAST_TYPE],
                CONF_ADD_SENSORS: user_input[CONF_ADD_SENSORS],
            },
            options={
                CONF_INTERVAL_OBSERVATION: 1,
                CONF_INTERVAL_FORECAST: 30,
            },
        )

    async def _show_setup_form(self, errors=None):
        """Show the setup form to the user."""
        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema(
                {
                    vol.Required(CONF_STATION_ID): int,
                    vol.Required(CONF_API_TOKEN): str,
                    vol.Required(
                        CONF_FORECAST_TYPE, default=FORECAST_TYPE_DAILY
                    ): vol.In(VALID_FORECAST_TYPES),
                    vol.Required(CONF_ADD_SENSORS, default=True): bool,
                }
            ),
            errors=errors or {},
        )


class OptionsFlowHandler(config_entries.OptionsFlow):
    """Handle options."""

    def __init__(self, config_entry):
        """Initialize options flow."""
        self.config_entry = config_entry

    async def async_step_init(self, user_input=None):
        """Manage the options."""
        if user_input is not None:
            return self.async_create_entry(title="", data=user_input)

        return self.async_show_form(
            step_id="init",
            data_schema=vol.Schema(
                {
                    vol.Optional(
                        CONF_INTERVAL_OBSERVATION,
                        default=self.config_entry.data.get(
                            CONF_INTERVAL_OBSERVATION, 1
                        ),
                    ): str,
                    vol.Optional(
                        CONF_INTERVAL_FORECAST,
                        default=self.config_entry.data.get(CONF_INTERVAL_FORECAST, 30),
                    ): str,
                }
            ),
        )
