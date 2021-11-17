# WeatherFlow Weather for Home Assistant
![GitHub release (latest by date)](https://img.shields.io/github/v/release/briis/hass-weatherflow?style=flat-square) [![hacs_badge](https://img.shields.io/badge/HACS-Custom-41BDF5.svg)](https://github.com/hacs/integration) [![](https://img.shields.io/badge/COMMUNITY-FORUM-success?style=flat-square)](https://community.home-assistant.io/t/smartweather-get-local-weather-data-combined-with-ai-powered-forecast/105151)

The WeatherFlow integration adds support for retreiving weather data from a Personal Weatherstation manufactured by [WeatherFlow](https://weatherflow.com/tempest-weather-system/) using a [REST API](https://weatherflow.github.io/Tempest/api/swagger/).

There is currently support for the following device types within Home Assistant:

* Weather
  * Two Weather entities will be created per station. One showing an hour based forecast and one showing a day based forecast.
* Sensor
  * A whole range of individual sensors will be available. for a complete list of the sensors, see the list below.
* Binary Sensor
  * A few binary sensors will be available, that can be used to trigger automations, if f.ex. it starts raining.

## Installation

### HACS installation
This Integration is not part of the default HACS store yet, but you can add it as a Custom repository in HACS by doing the following:

1. Go to HACS in your HA installation, and click on Integrations
2. Click the three vertical dots in the upper right corner, and select Custom repositories
3. Add https://github.com/briis/hass-weatherflow and select Integration as Category, and then click Add

You should now be able to find this Integration in HACS. (Most times you need to do a Hard Refresh of the browser before it shows up)

### Manual Installation

To add WeatherFlow to your installation, create this folder structure in your /config directory:

`custom_components/weatherflow`.

Then drop the following files into that folder:

```yaml
__init__.py
binary_sensor.py
config_flow.py
const.py
entity.py
manifest.json
sensor.py
weather.py
translation (Directory with all files)
```
## Available Sensors

Here is the list of sensors that the program generates. Calculated Sensor means, if No, then data comes directly from the Weather Station, if yes, it is a sensor that is derived from some of the other sensors.

All entities are prefixed with `weatherflow_` and names are prefixed with `Weatherflow`

| Sensor ID   | Name   | Description   | Calculated Sensor   |
| --- | --- | --- | --- |
| absolute_humidity | Absolute Humidity | The amount of water per volume of air | Yes |
| air_density | Air Density | The Air density | No |
| air_temperature | Temperature | Outside Temperature | No |
| voltage_air | Voltage AIR | The voltage on the AIR unit (If present) | No |
| battery_air | Battery AIR | The battery level on the AIR unit (If present) | Yes |
| voltage_sky | Voltage SKY | voltage on the SKY unit (If present) | No |
| battery_sky | Battery SKY | The battery level on the SKY unit (If present) | Yes |
| voltage_tempest | Voltage TEMPEST | The voltage on the TEMPEST unit (If present) | No |
| battery_tempest | Battery TEMPEST | The battery level on the TEMPEST unit (If present) | Yes |
| beaufort | Beaufort Scale | Beaufort scale is an empirical measure that relates wind speed to observed conditions at sea or on land | Yes ||
| delta_t | Delta T | Difference between Air Temperature and Wet Bulb Temperature | No |
| dewpoint | Dew Point | Dewpoint in degrees | No |
| feelslike | Feels Like Temperature | The apparent temperature, a mix of Heat Index and Wind Chill | No |
| heat_index | Heat Index | How warm does it feel? | No |
| wind_chill | Wind Chill | How cold does it feel? | No |
| wet_bulb_temperature | Wet Bulb Temperature | Temperature of a parcel of air cooled to saturation (100% relative humidity) | No |
| lightning_strike_count | Lightning Count | Number of lightning strikes in the last minute | No |
| lightning_strike_count_1hr | Lightning Count (Last hour) | Number of lightning strikes during the last hour | No |
| lightning_strike_count_3hr | Lightning Count (3 hours) | Number of lightning strikes the last 3 hours | No |
| lightning_strike_last_distance | Lightning Distance | Distance of the last strike | No |
| lightning_strike_last_epoch | Last Lightning Strike | When the last lightning strike occurred | No |
| precip | Rain | reported the last minute | No |
| precip_rate | Rain Rate | How much is it raining right now | Yes |
| precip_accum_last_1hr | Rain in the last hour | Total rain accumulation for the last hour | No |
| precip_accum_local_day | Rain Today | Total rain for the current day. (Reset at midnight) | No |
| precip_accum_local_yesterday | Rain Yesterday | Total rain for yesterday (Reset at midnight) | No |
| precip_minutes_local_day | Rain Duration (Today) | Total rain minutes for the current day. (Reset at midnight) | No |
| precip_minutes_local_yesterday | Rain Duration (Yesterday) | Total rain minutes yesterday | No |
| relative_humidity | Humidity | Relative Humidity | No |
| pressure_trend | Pressure Trend | Returns Steady, Falling or Rising determined by the rate of change over the past 3 hours| No |
| barometric_pressure | Barometric Pressure | The Barometric pressure | No |
| sealevel_pressure | Station Pressure | Preasure measurement at Sea Level | No |
| station_pressure | Station Pressure | Pressure measurement where the station is located | No |
| brightness | Brightness | How much the incident light illuminates the surface | No |
| solar_radiation | Solar Radiation | Electromagnetic radiation emitted by the sun | No |
| uv | UV Index | The UV index | No |
| visibility | Visibility | Distance to the horizon | Yes |
| wind_avg | Wind Speed Avg | Average wind speed for the last minute | No |
| wind_direction | Wind Direction | Current measured Wind bearing in degrees | No |
| wind_gust | Wind Gust | Highest wind speed for the last minute | No |
| wind_lull | Wind Lull | Lowest wind for the last minute | No |

## Available Binary Sensors

Here is the list of binary sensors that the program generates. These sensors are all calculated based on values from other sensors

All entities are prefixed with `weatherflow_` and names are prefixed with `Weatherflow`

| Sensor ID   | Name   | Description   |
| --- | --- | --- |
| is_freezing | Is Freezing | Is the Temperature below freezing point |
| is_raining | Is Raining | Is it raining outside |

## Available Weather Entities

Here is the list of Weather Entities that the program generates. With the exception of the condition state and the icon, the values for the current condition are equal to the Sensor values, so the Weather entity displayes realtime values and the forecast for either the next days or the next hours.

All entities are prefixed with `weatherflow_` and names are prefixed with `Weatherflow`

| Sensor ID   | Name   | Description   |
| --- | --- | --- |
| day_based_forecast | Day Based Forecast | A weather entity with Forecast for today and the next 9 days |
| hourly_based_forecast | Hour Based Forecast | A weather entity with Forecast for the next 240 hours |

