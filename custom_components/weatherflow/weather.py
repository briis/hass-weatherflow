"""This module provides a Weather Entity for WeatherFlow."""
from __future__ import annotations

import logging

from homeassistant.components.weather import (
    ATTR_FORECAST_CONDITION,
    ATTR_FORECAST_PRECIPITATION,
    ATTR_FORECAST_PRECIPITATION_PROBABILITY,
    ATTR_FORECAST_TEMP,
    ATTR_FORECAST_TEMP_LOW,
    ATTR_FORECAST_TIME,
    ATTR_FORECAST_WIND_BEARING,
    ATTR_FORECAST_WIND_SPEED,
    WeatherEntity,
    WeatherEntityDescription,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import TEMP_CELSIUS
from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator
from pyweatherflowrest.data import (
    ForecastDailyDescription,
    ForecastHourlyDescription,
    StationDescription,
)

from .const import CONDITION_CLASSES, DOMAIN
from .entity import WeatherFlowEntity

_WEATHER_DAILY = "weather_daily"
_WEATHER_HOURLY = "weather_hourly"

_LOGGER = logging.getLogger(__name__)

WEATHER_TYPES: tuple[WeatherEntityDescription, ...] = (
    WeatherEntityDescription(
        key=_WEATHER_DAILY,
        name="Day based Forecast",
    ),
    WeatherEntityDescription(
        key=_WEATHER_HOURLY,
        name="Hourly based Forecast",
    ),
)


def format_condition(condition: str):
    """Map the conditions provided by the weather API to those supported by the frontend."""
    return next(
        (k for k, v in CONDITION_CLASSES.items() if condition in v),
        None,
    )


async def async_setup_entry(
    hass: HomeAssistant, entry: ConfigEntry, async_add_entities
) -> None:
    """Add a weather entity from a config_entry."""
    entry_data = hass.data[DOMAIN][entry.entry_id]
    weatherflowapi = entry_data["weatherflowapi"]
    coordinator = entry_data["coordinator"]
    forecast_coordinator = entry_data["forecast_coordinator"]
    station_data: StationDescription = entry_data["station_data"]
    unit_descriptions = entry_data["unit_descriptions"]

    entities = []
    for description in WEATHER_TYPES:
        entities.append(
            WeatherFlowWeatherEntity(
                weatherflowapi,
                coordinator,
                forecast_coordinator,
                station_data,
                description,
                entry,
                unit_descriptions,
            )
        )

        _LOGGER.debug(
            "Adding weather entity %s",
            description.name,
        )

    async_add_entities(entities)


class WeatherFlowWeatherEntity(WeatherFlowEntity, WeatherEntity):
    """A WeatherFlow Weather Entity."""

    def __init__(
        self,
        weatherflowapi,
        coordinator: DataUpdateCoordinator,
        forecast_coordinator: DataUpdateCoordinator,
        station_data: StationDescription,
        description: WeatherEntityDescription,
        entries: ConfigEntry,
        unit_descriptions,
    ):
        """Initialize an WeatherFlow sensor."""
        super().__init__(
            weatherflowapi,
            coordinator,
            forecast_coordinator,
            station_data,
            description,
            entries,
        )
        self.unit_descriptions = unit_descriptions
        self.daily_forecast = self.entity_description.key in _WEATHER_DAILY
        self._attr_name = f"{DOMAIN.capitalize()} {self.entity_description.name}"
        self._attr_temperature = self.coordinator.data.air_temperature
        self._attr_temperature_unit = TEMP_CELSIUS
        self._attr_pressure = self.coordinator.data.sea_level_pressure
        self._attr_humidity = self.coordinator.data.relative_humidity
        self._attr_visibility = self.coordinator.data.visibility
        self._attr_wind_speed = self.forecast_coordinator.data.wind_avg
        self._attr_wind_bearing = self.forecast_coordinator.data.wind_direction
        self._attr_condition = format_condition(self.forecast_coordinator.data.icon)

    @property
    def forecast(self):
        """Return the forecast array."""
        data = []
        if self.daily_forecast:
            forecast_data: ForecastDailyDescription = (
                self.forecast_coordinator.data.forecast_daily
            )
            for item in forecast_data:
                data.append(
                    {
                        ATTR_FORECAST_TIME: item.utc_time,
                        ATTR_FORECAST_TEMP: item.air_temp_high,
                        ATTR_FORECAST_TEMP_LOW: item.air_temp_low,
                        ATTR_FORECAST_PRECIPITATION: item.precip,
                        ATTR_FORECAST_PRECIPITATION_PROBABILITY: item.precip_probability,
                        ATTR_FORECAST_CONDITION: format_condition(item.icon),
                        ATTR_FORECAST_WIND_SPEED: item.wind_avg,
                        ATTR_FORECAST_WIND_BEARING: item.wind_direction,
                    }
                )
            return data

        forecast_data: ForecastHourlyDescription = (
            self.forecast_coordinator.data.forecast_hourly
        )
        for item in forecast_data:
            data.append(
                {
                    ATTR_FORECAST_TIME: item.utc_time,
                    ATTR_FORECAST_TEMP: item.air_temperature,
                    ATTR_FORECAST_PRECIPITATION: item.precip,
                    ATTR_FORECAST_PRECIPITATION_PROBABILITY: item.precip_probability,
                    ATTR_FORECAST_CONDITION: format_condition(item.icon),
                    ATTR_FORECAST_WIND_SPEED: item.wind_avg,
                    ATTR_FORECAST_WIND_BEARING: item.wind_direction,
                }
            )
        return data
