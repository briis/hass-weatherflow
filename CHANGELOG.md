# Change Log
All notable changes to this project will be documented in this file.

## [1.0.8] - NOT RELEASED

### Changed

- Converted all DEVICE_CLASS values to `SensorDeviceClass.DEVICE_CLASS`. This includes two new Device Classes SPEED and DISTANCE, which makes it possible to change the Unit of Measurement directly from the GUI.
- Bumped minimum required Home Assistant version to 2022.11.0b0 due to the changes in this release

### Fixed

- Fix [#47](https://github.com/briis/hass-weatherflow/issues/47) WARNING Detected integration that accesses the is_metric property of the unit system.

## [1.0.7] - 2022-08-04

### Added

- German translation for Config Flow and Sensors. Thanks to @maccowley.

### Changed

- Updated README file. Fixed a few typos. Thank you to @notmayo.

### Fixed

- Unit for Absolute Humidity was wrongly set to `%`. Is now changed to `g/m^3`.

## [1.0.6] - 2022-07-02

**You must be running Home Assistant 2022.7.0 before applying this update.**

### Fixed

- Fixing `is overriding deprecated methods on an instance of WeatherEntity` message that will start showing up in the log.


## [1.0.5] - 2022-05-26

### Fixed

- Fixing deprecated `async_get_registry` that will start showing up in HA 2022.6


## [1.0.4] - 2022-02-22

### Added

- Added czech translation. Thank you to @kocour

## [1.0.3] - 2022-01-27

### Fixed

- In rare occasions the forecast icon is not present in data supplied from WeatherFlow. Will now be set to Cloudy as default.


## [1.0.2] - 2022-01-02

### Fixed

- The format of the forecast items could not work with the *weather template*. This was caused by the `datetime` attribute not being a string but a DateTime object.

### Changed

- Moved all shared attributes to the common entity definitions
- Some code cleanup and linting.
- Removed `sunrise` and `sunset` attributes from the daily forecast. Use the `sun.sun` component instead.
- Issue [#23](https://github.com/briis/hass-weatherflow/issues/23) Changed error description when we could not retrieve data from WeatherFlow.


## [1.0.1] - 2021-12-30

### Fixed

- Issue [#22](https://github.com/briis/hass-weatherflow/issues/22) *Feels Like* forecast temperature had wrong value when displayed with Imperial Units.

## [1.0.0] - 2021-12-29

After a lot of testing I believe we are now at a point where this module will be called 1.0.0 as it is stable and delivers as expected.

### Added

- The Hourly Forecast has the following new Attributes:
  - `wind_gust`
  - `uv_index`
  - `Feels_like`
- The Daily Forecast has the following new Attributes:
  - `sunrise`
  - `sunset`
- New sensor called `freezing_line`. It holds the altitude above sea level where snow is possible in meters or feet, depending on unit system. Thanks to @GlennGoddard for the formula.
- New sensor `cloud_base`. It holds the cloud height altitude above sea level in meters or feet, depending on unit system. Thanks to @GlennGoddard for the formula.


## [0.1.18] - 2021-12-22

### Changes

- Implemented better error handling to avoid the the program crashing. Due to the way WeatherFlow delivers result back from the REST call, it is not always possible to determine the exact cause of the error. Please always check that Station Id and Personal Token work together.

## [0.1.17] - 2021-12-21

### Fixed

- Issue #18. Some times the list of devices attached to a Hub, does not contain a `device_type`, and that would make the Integration crash.


## [0.1.16] - 2021-12-19

### Added

- Issue #16. Option to configurate how many hours are loaded for the Hourly based forecast. Minimum is 24 hours, maximum 240 hours and default is 48 hours. Go to the Integration page and click on CONFIGURE on the WeatherFlow integration, and then pull the slider to the hours you want.

## [0.1.15] - 2021-12-16

### Added

- A new sensor called `station_information` is added. This sensor shows the name of the Station as state, and then has all the data about the station and attached devices in the attributes. Similar to the `station_name` in the SmartWeather integration.
- New sensors `precipitation_duration_yesterday_rain_checked`, `precipitation_yesterday_rain_checked`, `precipitation_today_rain_checked`. These values will only appear for stations located in the US, as they are depended on *Rain Check* and that only works in the US. Holding calibated precipitation data.

### Changed

- Fixing issue #15, where Home Assistant sometimes added a warning about to long an update time for the Hourly forecast. The number of hours has now been reduced to the next 48 hours, instead of the next 240 hours.

## [0.1.14] - 2021-12-14

### Added

- A new sensor called `battery_mode` is added. This sensor reports a mode between 0 and 3, and the description for the mode is added as an attribute to the sensor. Basically it shows how the Tempest device operates with the current Voltage. You can read more about this on the [WeatherFlow Website](https://help.weatherflow.com/hc/en-us/articles/360048877194-Solar-Power-Rechargeable-Battery). **This sensor is only available for Tempest devices**

### Changed
- Closing issue #14. Introducing better handling of error when dataset returned from WeatherFlow is empty. Can happen if the station has been offline for a while.


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
