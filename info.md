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

**NOTE**: This integration replaces the `WeatherFlow Smart Weather` integration, which will soon be removed from HACS and marked as *Archieved*. This new integration is completely rewritten, both for the IO Module (`pyweatherflowrest`) that talks to WeatherFlow, and the Home Assistant integration itself, which is now up to date with all the latest coding practices in Home Assistant.

## Configuration

This custom integration can only be configured from the UI. Once installed and Home Assistant has been restarted:
- Go to *Configuration* and *Integrations*
- Click the `+ ADD INTEGRATION` button in the lower right corner.
- Search for WeatherFlow and click the integration.
- When loaded, there will be a configuration box, where you have to enter your *Station ID* and a *Personal Token* to get access to your data. When entered click *Submit* and the Integration will loadd all the entities.
- If you want to change the update frequencies for the realtime data and forecast data, you can now do this, by clicking `CONFIGURE` in the lower left corner of the integration.

For further information and installation instruction please see the [README](https://github.com/briis/hass-weatherflow/blob/main/README.md) on Github.
