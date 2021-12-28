# WeatherFlow Weather for Home Assistant
![GitHub release (latest by date)](https://img.shields.io/github/v/release/briis/hass-weatherflow?style=flat-square) [![hacs_badge](https://img.shields.io/badge/HACS-Default-orange.svg?style=flat-square)](https://github.com/custom-components/hacs) [![](https://img.shields.io/badge/COMMUNITY-FORUM-success?style=flat-square)](https://community.home-assistant.io/t/weatherflow-weather/368627)

The WeatherFlow integration adds support for retreiving weather data from a Personal Weatherstation manufactured by [WeatherFlow](https://weatherflow.com/tempest-weather-system/) using a [REST API](https://weatherflow.github.io/Tempest/api/swagger/).

There is currently support for the following device types within Home Assistant:

* Weather
  * Two Weather entities will be created per station. One showing an hour based forecast and one showing a day based forecast.
* Sensor
  * A whole range of individual sensors will be available. for a complete list of the sensors, see the list below.
* Binary Sensor
  * A few binary sensors will be available, that can be used to trigger automations, if f.ex. it starts raining.

## Table of Contents

1. [Installation](#installation)
    * [HACS Installation](#hacs-installation)
    * [Manuel Installation](#manuel-installation)
2. [Configuration](#configuration)
    * [Token for WeatherFlow](#token-for-weatherflow)
    * [Station ID](#station-id)
3. [Available Sensors](#available-sensors)
4. [Available Binary Sensors](#available-binary-sensors)
5. [Available Weather Entities](#available-weather-entities)
6. [Enable Debug Logging](#enable-debug-logging)
7. [Contribute to Development](#contribute-to-the-project-and-developing-with-a-devcontainer)
    * [Integration](#integration)
    * [Frontend](#frontend)

## Installation

### HACS installation

This Integration is part of the default HACS store. Search for *weatherflow weather* under *Integrations* and install from there. After the installation of the files you must restart Home Assistant, or else you will not be able to add WeatherFlow Weather from the Integration Page.

If you are not familiar with HACS, or haven't installed it, I would recommend to [look through the HACS documentation](https://hacs.xyz/), before continuing. Even though you can install the Integration manually, I would recommend using HACS, as you would always be reminded when a new release is published.

### Manuel installation

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
models.py
sensor.py
weather.py
translation (Directory with all files)
```

## Configuration
To add WeatherFlow Weather to your installation, do the following:
- Go to *Configuration* and *Integrations*
- Click the `+ ADD INTEGRATION` button in the lower right corner.
- Search for WeatherFlow and click the integration.
- When loaded, there will be a configuration box, where you have to enter your *Station ID* and a *Personal Token* to get access to your data. When entered click *Submit* and the Integration will load all the entities.

If you want to change the update frequencies for the realtime data and forecast data, this can be done by clicking `CONFIGURE` in the lower left corner of the WeatherFlow integration..

You can configure more than 1 instance of the Integration by using a different Station ID.

### Token for WeatherFlow
The WeatherFlow REST API requires a Token. Please [login with your account](https://tempestwx.com/settings/tokens) and create the token. Go to Settings and choose Data Authorizations (almost at the bottom). Create a personal access token and use that as Token (API key).

**Please Note**: The Token you create here will ONLY work with Stations that are registered under the same Login.

### Station ID
Each WeatherFlow Station you setup, will get a unique Station ID, this id is needed during configuration. To get your Station ID, [login with your account](https://tempestwx.com/settings/stations/), select the station on the list, and then click *Status*. Here you will find your Station ID.

## Available Sensors

Here is the list of sensors that the program generates. Calculated Sensor means, if No, then data comes directly from the Weather Station, if yes, it is a sensor that is derived from some of the other sensors. Not all sensors show up on all installations. It depends on the Physical Device you have and where in the world your station is located.

All entities are prefixed with `weatherflow_` and names are prefixed with `Weatherflow`

| Sensor ID   | Name   | Description   | Calculated Sensor   |
| --- | --- | --- | --- |
| absolute_humidity | Absolute Humidity | The amount of water per volume of air | Yes |
| air_density | Air Density | The Air density | No |
| air_temperature | Air Temperature | Outside Temperature | No |
| barometric_pressure | Barometric Pressure | The Barometric pressure | No |
| battery_air | Battery AIR | The battery level on the AIR unit (If present) | Yes |
| battery_sky | Battery SKY | The battery level on the SKY unit (If present) | Yes |
| battery_tempest | Battery TEMPEST | The battery level on the TEMPEST unit (If present) | Yes |
| battery_mode_tempest | Battery Mode TEMPEST | How the Tempest device operates with the current Voltage | Yes |
| beaufort | Beaufort Scale | Beaufort scale is an empirical measure that relates wind speed to observed conditions at sea or on land | Yes ||
| beaufort_description | Beaufort Description | A descriptive text for the current Beaufort level. | Yes ||
| brightness | Brightness | How much the incident light illuminates the surface | No |
| delta_t | Delta T | Difference between Air Temperature and Wet Bulb Temperature | No |
| dewpoint | Dew Point | Dewpoint in degrees | No |
| feelslike | Feels Like Temperature | The apparent temperature, a mix of Heat Index and Wind Chill | No |
| heat_index | Heat Index | How warm does it feel? | No |
| last_lightning_strike | Last Lightning Strike | When the last lightning strike occurred | No |
| last_lightning_strike_distance | Lightning Distance | Distance of the last strike | No |
| lightning_strike_count | Lightning Count | Number of lightning strikes in the last minute | No |
| lightning_strike_count_last_3_hours | Lightning Count (3 hours) | Number of lightning strikes the last 3 hours | No |
| lightning_strike_count_last_hour | Lightning Count (Last hour) | Number of lightning strikes during the last hour | No |
| precipitation_duration_today | Rain Duration (Today) | Total rain minutes for the current day. (Reset at midnight) | No |
| precipitation_duration_yesterday | Rain Duration (Yesterday) | Total rain minutes yesterday | No |
| precipitation_duration_yesterday_rain_checked | Rain Duration (Yesterday) Only if Rain Check enabled and in the US | Total rain minutes yesterday | No |
| precip_intensity | Rain Intensity | A descriptive text of how much is it raining right now | Yes |
| precipitation_last_hour | Rain in the last hour | Total rain accumulation for the last hour | No |
| precipitation_rate | Rain Rate | How much is it raining right now | Yes |
| precipitation_today | Rain Today | Total rain for the current day. (Reset at midnight) | No |
| precipitation_today_rain_checked | Rain Today | Total rain for the current day. (Reset at midnight) Only if Rain Check enabled and in the US | No |
| precipitation_yesterday | Rain Yesterday | Total rain for yesterday (Reset at midnight) | No |
| precipitation_yesterday_rain_checked | Rain Yesterday | Total rain for yesterday (Reset at midnight) Only if Rain Check enabled and in the US | No |
| pressure_trend | Pressure Trend | Returns Steady, Falling or Rising determined by the rate of change over the past 3 hours| No |
| relative_humidity | Humidity | Relative Humidity | No |
| sea_level_pressure | Station Pressure | Preasure measurement at Sea Level | No |
| solar_radiation | Solar Radiation | Electromagnetic radiation emitted by the sun | No |
| station_information | Station Information | Attributes show data about the physical devices present | No |
| station_pressure | Station Pressure | Pressure measurement where the station is located | No |
| uv_description | UV Description | A descriptive text for the current UV index | Yes |
| uv_index | UV Index | The UV index | No |
| visibility | Visibility | Distance to the horizon | Yes |
| voltage_air | Voltage AIR | The voltage on the AIR unit (If present) | No |
| voltage_sky | Voltage SKY | voltage on the SKY unit (If present) | No |
| voltage_tempest | Voltage TEMPEST | The voltage on the TEMPEST unit (If present) | No |
| wet_bulb_temperature | Wet Bulb Temperature | Temperature of a parcel of air cooled to saturation (100% relative humidity) | No |
| wind_cardinal | Wind Cardinal | Current measured Wind bearing as text | Yes |
| wind_chill | Wind Chill | How cold does it feel? | No |
| wind_direction | Wind Direction | Current measured Wind bearing in degrees | No |
| wind_gust | Wind Gust | Highest wind speed for the last minute | No |
| wind_gust_kmh | Wind Gust (km/h) | Highest wind speed for the last minute in km/h | No |
| wind_gust_knots | Wind Gust (knots) | Highest wind speed for the last minute in knots | No |
| wind_lull | Wind Lull | Lowest wind for the last minute | No |
| wind_lull_kmh | Wind Lull (km/h) | Lowest wind for the last minute in km/h | No |
| wind_lull_knots | Wind Lull (knots) | Lowest wind for the last minute in knots | No |
| wind_speed | Wind Speed Avg | Average wind speed for the last minute | No |
| wind_speed_kmh | Wind Speed Avg (km/h) | Average wind speed for the last minute in km/h | No |
| wind_speed_knots | Wind Speed Avg (knots) | Average wind speed for the last minute in knots | No |

## Available Binary Sensors

Here is the list of binary sensors that the program generates. These sensors are all calculated based on values from other sensors

All entities are prefixed with `weatherflow_` and names are prefixed with `Weatherflow`

| Sensor ID   | Name   | Description   |
| --- | --- | --- |
| is_freezing | Is Freezing | Is the Temperature below freezing point |
| is_lightning | Is Lightning | Has lighning strikes occured within the last minute |
| is_raining | Is Raining | Is it raining outside |

## Available Weather Entities

Here is the list of Weather Entities that the program generates. With the exception of the condition state and the icon, the values for the current condition are equal to the Sensor values, so the Weather entity displayes realtime values and the forecast for either the next days or the next hours. Both entities are installed.

All entities are prefixed with `weatherflow_` and names are prefixed with `Weatherflow`

| Sensor ID   | Name   | Description   |
| --- | --- | --- |
| day_based_forecast | Day Based Forecast | A weather entity with Forecast for today and the next 9 days |
| hourly_based_forecast | Hourly Based Forecast | A weather entity with Forecast for the next 48 hours |

## Enable Debug Logging

If logs are needed for debugging or reporting an issue, use the following configuration.yaml:

```yaml
logger:
  default: error
  logs:
    pyweatherflowrest: debug
    custom_components.weatherflow: debug
```

## CONTRIBUTE TO THE PROJECT AND DEVELOPING WITH A DEVCONTAINER

### Integration

1. Fork and clone the repository.
2. Open in VSCode and choose to open in devcontainer. Must have VSCode devcontainer prerequisites.
3. Run the command container start from VSCode terminal
4. A fresh Home Assistant test instance will install and will eventually be running on port 9124 with this integration running
5. When the container is running, go to http://localhost:9124 and the add WeatherFlow Weather from the Integration Page.

### Frontend

There are some sensors in this integration that provides a text as state which is not covered by the core Frontend translation. Example: `sensor.weatherflow_pressure_tend`, `sensor.weatherflow_uv_description` and `sensor.weatherflow_beaufort_description`.

As default the text in the Frontend is displayed in english if your language is not present in this integration, but if you want to help translate these texts in to a new language, please do the following:
- Go to the `translations` directory under `custom_components/weatherflow` and copy the file `sensor.en.json` to `sensor.YOUR_LANGUAGE_CODE.json` in a directory on your computer.
- Edit the file and change all the descriptions to your language.
- Make a Pull request in this Github and attach your new file.

The same procedure applies for the Configuration flow, follow the above procedure, just copy `en.json` to `YOUR_LANGUAGE_CODE.json`.
