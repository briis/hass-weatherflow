"""This component provides sensors for WeatherFlow."""
from __future__ import annotations

from dataclasses import dataclass
import logging

from homeassistant.components.sensor import SensorEntity, SensorEntityDescription
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import (
    DEGREE,
    DEVICE_CLASS_BATTERY,
    DEVICE_CLASS_HUMIDITY,
    DEVICE_CLASS_ILLUMINANCE,
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

    device_type: set[str]


@dataclass
class WeatherFlowSensorEntityDescription(
    SensorEntityDescription, WeatherFlowRequiredKeysMixin
):
    """Describes WeatherFlow Sensor entity."""


SENSOR_TYPES: tuple[WeatherFlowSensorEntityDescription, ...] = (
    WeatherFlowSensorEntityDescription(
        key="utc_time",
        name="UTC Time",
        icon="mdi:clock",
        entity_category=ENTITY_CATEGORY_DIAGNOSTIC,
        device_class=DEVICE_CLASS_DATE,
        device_type="AIR",
    ),
    WeatherFlowSensorEntityDescription(
        key="air_temperature",
        name="Air Temperature",
        native_unit_of_measurement=TEMP_CELSIUS,
        device_class=DEVICE_CLASS_TEMPERATURE,
        entity_category=ENTITY_CATEGORY_DIAGNOSTIC,
        device_type="AIR",
    ),
    WeatherFlowSensorEntityDescription(
        key="wind_direction",
        name="Wind Direction",
        icon="mdi:compass",
        native_unit_of_measurement=DEGREE,
        entity_category=ENTITY_CATEGORY_DIAGNOSTIC,
        device_type="SKY",
    ),
    WeatherFlowSensorEntityDescription(
        key="wind_gust",
        name="Wind Gust",
        icon="mdi:weather-windy",
        native_unit_of_measurement="m/s",
        entity_category=ENTITY_CATEGORY_DIAGNOSTIC,
        device_type="SKY",
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

    entities = []
    for description in SENSOR_TYPES:
        entities.append(
            WeatherFlowSensor(weatherflowapi, coordinator, station_data, description)
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
        coordinator,
        station_data,
        description: WeatherFlowSensorEntityDescription,
    ):
        """Initialize an WeatherFlow sensor."""
        super().__init__(weatherflowapi, coordinator, station_data, description)
        self._attr_name = f"{DOMAIN.capitalize()} {self.entity_description.name}"

    @property
    def native_value(self):
        """Return the state of the sensor."""
        return self._device_value
