"""This component provides sensors for WeatherFlow."""
from __future__ import annotations

from dataclasses import dataclass
import logging

from homeassistant.components.sensor import SensorEntity, SensorEntityDescription
from homeassistant.config_entries import ConfigEntry
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator
from homeassistant.const import (
    DEGREE,
    DEVICE_CLASS_BATTERY,
    DEVICE_CLASS_HUMIDITY,
    DEVICE_CLASS_ILLUMINANCE,
    DEVICE_CLASS_PRESSURE,
    DEVICE_CLASS_SIGNAL_STRENGTH,
    DEVICE_CLASS_TEMPERATURE,
    DEVICE_CLASS_DATE,
    ENTITY_CATEGORY_DIAGNOSTIC,
    TEMP_CELSIUS,
)
from homeassistant.core import HomeAssistant

from .const import (
    DOMAIN,
)
from .entity import WeatherFlowEntity


@dataclass
class WeatherFlowRequiredKeysMixin:
    """Mixin for required keys."""

    unit_type: str


@dataclass
class WeatherFlowSensorEntityDescription(
    SensorEntityDescription, WeatherFlowRequiredKeysMixin
):
    """Describes WeatherFlow Sensor entity."""


SENSOR_TYPES: tuple[WeatherFlowSensorEntityDescription, ...] = (
    WeatherFlowSensorEntityDescription(
        key="air_temperature",
        name="Air Temperature",
        device_class=DEVICE_CLASS_TEMPERATURE,
        entity_category=ENTITY_CATEGORY_DIAGNOSTIC,
        native_unit_of_measurement=TEMP_CELSIUS,
        unit_type="none",
    ),
    WeatherFlowSensorEntityDescription(
        key="barometric_pressure",
        name="Barometric Pressure",
        device_class=DEVICE_CLASS_PRESSURE,
        entity_category=ENTITY_CATEGORY_DIAGNOSTIC,
        unit_type="pressure",
    ),
    WeatherFlowSensorEntityDescription(
        key="sea_level_pressure",
        name="Sea Level Pressure",
        device_class=DEVICE_CLASS_PRESSURE,
        entity_category=ENTITY_CATEGORY_DIAGNOSTIC,
        unit_type="pressure",
    ),
    WeatherFlowSensorEntityDescription(
        key="station_pressure",
        name="Station Pressure",
        device_class=DEVICE_CLASS_PRESSURE,
        entity_category=ENTITY_CATEGORY_DIAGNOSTIC,
        unit_type="pressure",
    ),
    WeatherFlowSensorEntityDescription(
        key="wind_direction",
        name="Wind Direction",
        icon="mdi:compass",
        native_unit_of_measurement=DEGREE,
        entity_category=ENTITY_CATEGORY_DIAGNOSTIC,
        unit_type="none",
    ),
    WeatherFlowSensorEntityDescription(
        key="wind_gust",
        name="Wind Gust",
        icon="mdi:weather-windy",
        entity_category=ENTITY_CATEGORY_DIAGNOSTIC,
        unit_type="length",
    ),
)


_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(
    hass: HomeAssistant, entry: ConfigEntry, async_add_entities
) -> None:
    """Set up sensors for UniFi Protect integration."""
    entry_data = hass.data[DOMAIN][entry.entry_id]
    weatherflowapi = entry_data["weatherflowapi"]
    coordinator = entry_data["coordinator"]
    station_data = entry_data["station_data"]
    unit_descriptions = entry_data["unit_descriptions"]

    entities = []
    for description in SENSOR_TYPES:
        entities.append(
            WeatherFlowSensor(
                weatherflowapi,
                coordinator,
                station_data,
                description,
                entry,
                unit_descriptions,
            )
        )

        _LOGGER.debug(
            "Adding sensor entity %s",
            description.name,
        )

    async_add_entities(entities)


class WeatherFlowSensor(WeatherFlowEntity, SensorEntity):
    """A WeatherFlow Sensor."""

    def __init__(
        self,
        weatherflowapi,
        coordinator: DataUpdateCoordinator,
        station_data,
        description: WeatherFlowSensorEntityDescription,
        entries: ConfigEntry,
        unit_descriptions,
    ):
        """Initialize an WeatherFlow sensor."""
        super().__init__(
            weatherflowapi, coordinator, station_data, description, entries
        )
        self._attr_name = f"{DOMAIN.capitalize()} {self.entity_description.name}"
        if self.entity_description.native_unit_of_measurement is None:
            self._attr_native_unit_of_measurement = unit_descriptions[
                self.entity_description.unit_type
            ]

    @property
    def native_value(self):
        """Return the state of the sensor."""
        return (
            getattr(self.coordinator.data, self.entity_description.key)
            if self.coordinator.data
            else None
        )
