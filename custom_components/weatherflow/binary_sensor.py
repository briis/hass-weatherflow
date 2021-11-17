"""This component provides binary sensors for WeatherFlow."""
from __future__ import annotations

import logging

from homeassistant.components.binary_sensor import (
    BinarySensorEntity,
    BinarySensorEntityDescription,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator
from pyweatherflowrest.data import StationDescription

from .const import DOMAIN
from .entity import WeatherFlowEntity

_LOGGER = logging.getLogger(__name__)

BINARY_SENSOR_TYPES: tuple[BinarySensorEntityDescription, ...] = (
    BinarySensorEntityDescription(
        key="is_freezing",
        name="Is Freezing",
        icon="mdi:snowflake-alert",
    ),
    BinarySensorEntityDescription(
        key="is_raining",
        name="Is Raining",
        icon="mdi:water-percent-alert",
    ),
)


async def async_setup_entry(
    hass: HomeAssistant, entry: ConfigEntry, async_add_entities
) -> None:
    """Set up sensors for UniFi Protect integration."""
    entry_data = hass.data[DOMAIN][entry.entry_id]
    weatherflowapi = entry_data["weatherflowapi"]
    coordinator = entry_data["coordinator"]
    forecast_coordinator = entry_data["forecast_coordinator"]
    station_data: StationDescription = entry_data["station_data"]

    entities = []
    for description in BINARY_SENSOR_TYPES:
        entities.append(
            WeatherFlowBinarySensor(
                weatherflowapi,
                coordinator,
                forecast_coordinator,
                station_data,
                description,
                entry,
            )
        )

        _LOGGER.debug(
            "Adding binary sensor entity %s",
            description.name,
        )

    async_add_entities(entities)


class WeatherFlowBinarySensor(WeatherFlowEntity, BinarySensorEntity):
    """A WeatherFlow Binary Sensor."""

    def __init__(
        self,
        weatherflowapi,
        coordinator: DataUpdateCoordinator,
        forecast_coordinator: DataUpdateCoordinator,
        station_data: StationDescription,
        description: BinarySensorEntityDescription,
        entries: ConfigEntry,
    ):
        """Initialize an WeatherFlow binary sensor."""
        super().__init__(
            weatherflowapi,
            coordinator,
            forecast_coordinator,
            station_data,
            description,
            entries,
        )
        self._attr_name = f"{DOMAIN.capitalize()} {self.entity_description.name}"

    @property
    def is_on(self):
        """Returns state of the sensor."""
        return getattr(self.coordinator.data, self.entity_description.key)
