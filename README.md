# python-mqtt-cayenne-bridge
Bridge between a local mqtt network (using eg. mosquitto) and the cayenne.mydevices.com cloud servce.

# Installation

```bash
git clone https://github.com/daniel-falk/python-mqtt-cayenne-bridge.git
cd python-mqtt-cayenne-bridge
virtualenv -p python3 .env
source .env/bin/activate
pip install -e .
```

## Autostart with systemd

Edit the systemd unitfile as needed to get absolute paths to your python module.
Then move/copy it to your systemd folder, eg:
```bash
mv cayennebridge.service /etc/systemd/system
sudo systemctl daemon-reload
sudo systemctl enable cayennebridge.service
sudo systemctl start cayennebridge.service
```

Check the status (use sudo to see the tail of the journal as well). if everything works it should look something like:
```bash
sudo systemctl status cayennebridge.service
● cayennebridge.service - Bridge messages between Cayenne, mydevices.com, and local MQTT.
   Loaded: loaded (/etc/systemd/system/cayennebridge.service; enabled)
   Active: active (running) since Thu 2017-06-29 20:48:20 CEST; 24min ago
 Main PID: 21562 (python)
   CGroup: /system.slice/cayennebridge.service
           └─21562 /home/pi/cayennebridge/.env/bin/python -mcayennebridge

Jun 29 20:48:24 raspberrypi python[21562]: Local mqtt sniffer started
Jun 29 20:48:24 raspberrypi python[21562]: Connected to mqtt (Local MQTT)
Jun 29 20:48:24 raspberrypi python[21562]: All workers started. Num cayenne client workers is 2
Jun 29 20:48:24 raspberrypi python[21562]: Subscribing to topic: cmdres/hall/+ for Local MQTT
Jun 29 20:48:24 raspberrypi python[21562]: Subscribing to topic: home/occupancy for Local MQTT
Jun 29 20:48:25 raspberrypi python[21562]: Change in occupancy: home/occupancy -> 1
Jun 29 20:48:25 raspberrypi python[21562]: Connected to mqtt (Hall Light)
Jun 29 20:48:25 raspberrypi python[21562]: Subscribing to topic: v1/******/things/*****/cmd/+ for Hall Light
Jun 29 20:48:25 raspberrypi python[21562]: Connected to mqtt (Occupancy [784])
Jun 29 20:48:25 raspberrypi python[21562]: Subscribing to topic: v1/*****/things/*****/cmd/+ for Occupancy [784]
```

# Run module manually

Run manually
```bash
source .env/bin/activate
python -m cayennebridge
```
