# Ventilation App

## Introduction
This app represents the frontend of a Raspbarry-Pi controlled Ventilation System, designed to keep a steady humidity level in the area the
sensors are place.

The Raspberry is using a temperature and a humidity sensor and sends the data to the Servers REST API, which displays the current data, aswell as history.
If a certain threshold of humidity is breached, the server sends a signal to api, which sends an event back to the Pi to trigger the ventilation.

![Architecture](/Ventilation/Doc/architecture.PNG?raw=true "Optional Title")

## User Components

- Python Framework Flask
- Azure Cloud
- Azure DocumentDB as NoSQL Json Storage for sensor data
- Pusher API for Realtime
communication with the Raspberry Pi
- OpenWeatherMap.org for live weather data or current location
- Ruby, for Raspberry PI development
- RubyGem library dhtsensorffi for the DHT22 sensor
- Die RubyGem REST client for communication with web services
- rcswitchpi and wiringPi zum access der ventilation system
- Raspbian as OS of the Raspberry PI
 
