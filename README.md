# Broadlink AC Home Assistant Integration

Control Broadlink based Air Conditioners directly from Home Assistant. 

Based on https://github.com/liaan/broadlink_ac_mqtt but without requiring MQTT.

## Installation

Add as a custom repository to HACS with type Integration.

Or copy the repository into a `custom_components/broadlink_ac` folder in your config folder.

## Configuration

Restart Home Assistant and the go to:

Configuration > [Integrations](https://my.home-assistant.io/redirect/integrations/) > Add Integration > Broadlink AC

You will need to know the local IP and MAC of the air conditioner.
