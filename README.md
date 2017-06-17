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

# Run moduel

Run manually or add as @reboot to crontab
```bash
python -m cayennebridge
```
