# Change Log
All notable changes to this project will be documented in this file.

## [0.1.14] - Unreleased

### Added

- A new sensor called `battery_mode` is added. This sensor reports a mode between 0 and 3, and the description for the mode is added as an attribute to the sensor. Basically it shows how the Tempest device operates with the current Voltage. You can read more about this on the [WeatherFlow Website](https://help.weatherflow.com/hc/en-us/articles/360048877194-Solar-Power-Rechargeable-Battery). **This sensor is only available for Tempest devices**

## [0.1.13] - 2021-12-09

### Fixed

- Issue #13. Added 5 decimals to Air Density, for both Metric and Imperial units.


## [0.1.12] - 2021-12-07

### Fixed

- Issue #12. If no wind values where supplied - typically when the Tempest unit is saving battery - the integration would crash on startup.
- Update intervals where not saved between runs.
- Forecast data was never updated, only loaded on startup.
- Issue #11. DeltaT values where wrong when using Imperial Units.
- Issue #11. Air Density Values were wrong when using Imperial Units.

### Changed

- Issue #11. All Barometric values are now returned with 3 decimals when using Imperial units.


## [0.1.11] - 2012-12-06

### Fixed

- Issue #9. Fixing wrong Temperature values when using Imperial Unit System.

### Changed

- Changed miles per hour unit to mph, to be in line with standard Home Assistant
- Bumped `pyweatherflowrest` to 0.1.14

### Added

- Italian translation for Config Flow and Sensors. Thanks to @alexdelprete.


## [0.1.10] - 2012-12-05

### Added

- Issue #7. Dutch Language Translation for Sensor Values. Thanks to @dhover.

### Fixed

- Issue #8. Fixing crash when some data fields not present in result data.


## [0.1.9] - 2021-12-05

### Added

- Issue #3, New binary sensor called `is_lightning` added. Is True if lightning strokes have occurred within the last minute.
- Issue #4, Wind *sensors* will always be in m/s if Metric or mph if Imperial unit system. Now there are 2 extra sensors for each wind sensor that display the value in km/h and knots.
- Issue #7, Dutch Language Translation for Config Flow. Thanks to @dhover.

### Fixed

- Issue #6, For unknown reasons one specific data point was missing in the returned data from WeatherFlow. The error can not be replicated, but to ensure the system does not stop, we will no just return an empty value.


## [0.1.8] - 2021-11-30

## Fixed
- `weatherflow`: Issue #2, error occurs with some users when trying to retrieve `precip_icon` and `precip_type` from forecast. Both data points have been removed, as they are not used in this Integration.
- `pyweatherflowrest`: Bumped to 0.1.11.

## [0.1.7] - 2021-11-29

### Changed
- `weatherflow`: Re-factoring of the code base.
- `weatherflow`:Redesigning the development container and environment.
- `pyweatherflowrest`: Bumped to 0.1.10.

## [0.1.6] - 2021-11-18

### Added
- `weatherflow`: New sensor called `precip_intensity`, which displayes how much it is raining right now in a descriptive text.

### Changed
- `weatherflow`: Updated documentation.
- `pyweatherflowrest`: Bumped to 0.1.8.

## [0.1.5] - 2021-11-18

### Added
- `weatherflow`: Danish Language for config flow added.
- `weatherflow`: Frontend Translations are now in place for non-standard text based sensors like Pressure Trend and Beaufort Description.

### Changed
- `weatherflow`: Simplified Wind Conversion
- `weatherflow`: Code cleanup
- `pyweatherflowrest`: Bumped to 0.1.7. Removing `pytz` import. Adding text based sensors.

## [0.1.4] - 2021-11-17

### Fixed
- `weatherflow`: On some installation Home Assistant would report "*Unable to prepare setup for platform weatherflow.weather: Platform not found (No module named 'homeassistant.util.speed').*". This has now been fixed by replacing the Home Assistant function with a local conversion function.

## [0.1.3] - 2021-11-17

### Fixed
- `pyweatherflowrest`: Bumped to 0.1.4. Optimized Conversion and Calculation functions.
- `weatherflow`: Fixing all entities only got updated on startup
- `weatherflow`: Wind Speed on the Weather Card are now realtime data, and ensured to display the right value based on unit system.
