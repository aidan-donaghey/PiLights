# PiLights Readme File
## Mosquitto Set Up
On the server that will be running Mosquitto, you need to install it using 
"""
sudo apt-add-repository ppa:mosquitto-dev/mosquitto-ppa
sudo apt-get update
sudo apt-get install mosquitto
sudo apt-get install mosquitto-clients
"""
After this you can run it. After it runs it will actually only be visible to other localhost items.
To stop this you need to edit the `mosquitto.conf` file located at `/etc/mosquitto/`
