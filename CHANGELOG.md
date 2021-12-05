# Change Log
All notable changes to this project will be documented in this file.

## [0.1.9] - Unreleased

### Added

- Issue #3, New binary sensor called `is_lightning` added. Is True if lightning strokes have occurred within the last minute.
- Issue #4, Wind sensors will always be in m/s if Metric or mph if Imperial unit system. Now there is 2 extra sensors for each wind sensor that display the value in km/h or knots.
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
