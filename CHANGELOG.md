# Change Log
All notable changes to this project will be documented in this file.

## [0.1.6] - Unreleased

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
