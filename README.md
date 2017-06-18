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

Add a shellscript in your cayenne-bridge dir that will 

Create init file:
```bash
echo "[Unit]
Description=Connect local MQTT to cayenne.mydevices cloud service

[Service]
Type=simple
ExecStart=/home/pi/cayennebridge/.env/bin/python -m cayennebridge

[Install]
WantedBy=multi-user.target" > /lib/systemd/system/cayennebridge.service

sudo systemctl daemon-reload
sudo systemctl enable cayennebridge.service
sudo systemctl start cayennebridge.service
```

Check the status, if everything works it should look something like:
```bash
pi@raspberrypi:~ $ sudo systemctl status cayennebridge.service
● cayennebridge.service - Connect local MQTT to cayenne.mydevices cloud service
   Loaded: loaded (/lib/systemd/system/cayennebridge.service; enabled)
   Active: active (running) since Sun 2017-06-18 10:37:53 CEST; 1min 3s ago
 Main PID: 352 (python)
   CGroup: /system.slice/cayennebridge.service
           └─352 /home/pi/cayennebridge/.env/bin/python -m cayennebridge

Jun 18 10:37:53 raspberrypi systemd[1]: Starting Connect local MQTT to cayenne.mydevices cloud service...
Jun 18 10:37:53 raspberrypi systemd[1]: Started Connect local MQTT to cayenne.mydevices cloud service.
```

# Run module manually

Run manually
```bash
source .env/bin/activate
python -m cayennebridge
```
