"""Shared Entity definition for WeatherFlow Integration."""
from __future__ import annotations

import logging

import homeassistant.helpers.device_registry as dr
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import ATTR_ATTRIBUTION
from homeassistant.helpers.entity import DeviceInfo, Entity
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DEFAULT_ATTRIBUTION, DEFAULT_BRAND, DOMAIN

_LOGGER = logging.getLogger(__name__)


class WeatherFlowEntity(CoordinatorEntity, Entity):
    """Base class for unifi protect entities."""

    def __init__(
        self,
        weatherflowapi,
        coordinator,
        forecast_coordinator,
        station_data,
        description,
        entries: ConfigEntry,
    ):
        """Initialize the entity."""
        super().__init__(coordinator)

        if description:
            self.entity_description = description

        self.weatherflowapi = weatherflowapi
        self.coordinator = coordinator
        self.forecast_coordinator = forecast_coordinator
        self.station_data = station_data
        self.entry: ConfigEntry = entries
        self._attr_available = self.coordinator.last_update_success
        self._attr_unique_id = f"{description.key}_{self.station_data.key}"
        self._attr_device_info = DeviceInfo(
            manufacturer=DEFAULT_BRAND,
            via_device=(DOMAIN, self.entry.unique_id),
            connections={(dr.CONNECTION_NETWORK_MAC, self.entry.unique_id)},
            configuration_url=f"https://tempestwx.com/station/{self.station_data.key}/grid",
        )

    @property
    def extra_state_attributes(self):
        """Return common attributes"""
        return {
            ATTR_ATTRIBUTION: DEFAULT_ATTRIBUTION,
        }
