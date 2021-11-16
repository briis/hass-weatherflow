# WeatherFlow Weather for Home Assistant
![GitHub release (latest by date)](https://img.shields.io/github/v/release/briis/hass-weatherflow?style=flat-square) [![](https://img.shields.io/badge/COMMUNITY-FORUM-success?style=flat-square)](https://community.home-assistant.io/t/smartweather-get-local-weather-data-combined-with-ai-powered-forecast/105151)

The WeatherFlow integration adds support for retreiving weather data from a Personal Weatherstation manufactured by [WeatherFlow](https://weatherflow.com/tempest-weather-system/) using a [REST API](https://weatherflow.github.io/Tempest/api/swagger/).

There is currently support for the following device types within Home Assistant:

* Weather
  * Two Weather entities will be created per station. One showing an hour based forecast and one showing a day based forecast.
* Sensor
  * A whole range of individual sensors will be available. for a complete list of the sensors, see the list below.
* Binary Sensor
  * A few binary sensors will be available, that can be used to trigger automations, if f.ex. it starts raining.

**NOTE**: This integration replaces the `WeatherFlow Smart Weather` integration, which will soon be removed from HACS and marked as *Arhieved*. This new integration is completely rewritten, bot for the IO Module that talks to WeatherFlow, and the Home Assistant integration itself, which is now up to date with all the latest coding practices in Home Assistant.

For further information and installation instruction please see the [README](https://github.com/briis/hass-weatherflow/blob/main/README.md) on Github.
