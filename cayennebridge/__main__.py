import threading
from random import randint

from cayennebridge import conf, loc_mqtt
from cayennebridge.mqtt import Mqtt
from cayennebridge.models.light import Light
from cayennebridge.models.occupancy import Occupancy

def create_devices(loc_mqtt):
    devices = []
    base = conf._sections['CAYENNE']

    # Create the hall roof light device
    cayenne = base.copy()
    cayenne.update({'client_id':'af625f10-5068-11e7-90dc-cd639ca909a8'})
    hall_light = Light(loc_mqtt, cayenne)
    hall_light.local_topic = 'cmdres/hall/+'
    loc_mqtt.client.message_callback_add(hall_light.local_topic, hall_light.on_command_res)
    hall_light.name = 'Hall Light'
    devices.append(hall_light)

    # Create the home occupancy device
    cayenne = base.copy()
    cayenne.update({'client_id':'6690c390-5cec-11e7-a041-7d8fa03d7b64'})
    occupancy = Occupancy(loc_mqtt, cayenne)
    occupancy.local_topic = 'home/occupancy'
    loc_mqtt.client.message_callback_add(occupancy.local_topic, occupancy.on_change)
    devices.append(occupancy)

    return devices



# Create all devices we want to bridge

devices = create_devices(loc_mqtt)
print("Models created")


topics = [device.local_topic for device in devices if hasattr(device, 'local_topic')]
print("Local topics: {}".format(topics))
loc_mqtt_worker = threading.Thread(target=loc_mqtt.start, args=([topics]))
loc_mqtt_worker.start()
print("Local mqtt sniffer started")



# Start a mqtt connection to Cayenne for each device
cayenne_workers = []
for device in devices:
    s = device.cayenne
    nice_name = device.name if hasattr(device, 'name') else "{} [{}]".format(type(device).__name__, randint(100,999))
    mqtt = Mqtt(nice_name,
            s['host'],
            s['username'],
            s['password'],
            s['client_id'],
            int(s['keepalive']),
            int(s['min_retry_time']),
            int(s['max_retry_time']))
    topics = ['v1/{}/things/{}/cmd/+'.format(s['username'], s['client_id'])]
    mqtt.client.message_callback_add(topics[0], device.on_command)
    device.cayenne_mqtt = mqtt
    worker = threading.Thread(target=mqtt.start, args=([topics]))
    worker.start()
    cayenne_workers.append(worker)


print("All workers started. Num cayenne client workers is %d" % len(cayenne_workers))
loc_mqtt_worker.join(0)
for w in cayenne_workers:
    w.join(0)
