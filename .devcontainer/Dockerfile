FROM ghcr.io/ludeeus/devcontainer/integration:stable

RUN apt update \
    && sudo apt install -y libpcap-dev ffmpeg vim curl jq \
    && mkdir -p /opt \
    && cd /opt \
    && git clone --depth=1 -b dev https://github.com/home-assistant/core.git hass \
    && python3 -m pip --disable-pip-version-check install --upgrade ./hass \
    && python3 -m pip install flake8 pyweatherflowrest \
    && ln -s /workspaces/hass-weatherflow/custom_components/weatherflow /opt/hass/homeassistant/components/weatherflow
