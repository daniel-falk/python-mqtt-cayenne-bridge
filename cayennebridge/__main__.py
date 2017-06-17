import threading

from cayennebridge import conf, loc_mqtt
from cayennebridge.models.hall_light import HallLight
from cayennebridge.mqtt import Mqtt

def create_devices(loc_mqtt):
    devices = []
    base = conf._sections['CAYENNE']

    # Create the hall roof light device
    cayenne = base.copy()
    cayenne.update({'client_id':'af625f10-5068-11e7-90dc-cd639ca909a8'})
    hall_light = HallLight(loc_mqtt, cayenne)
    hall_light.local_topics = 'cmdres/hall/+'

    loc_mqtt.client.message_callback_add(hall_light.local_topics, hall_light.on_command_res)

    devices.append(hall_light)

    return devices



# Create all devices we want to bridge

devices = create_devices(loc_mqtt)
print("Models created")

topics = [device.local_topics for device in devices]
loc_mqtt_worker = threading.Thread(target=loc_mqtt.start, args=(topics))
loc_mqtt_worker.start()
print("Local mqtt sniffer started")



# Start a mqtt connection to Cayenne for each device
cayenne_workers = []
for device in devices:
    s = device.cayenne
    mqtt = Mqtt(s['host'], s['username'], s['password'], s['client_id'], s['keepalive'], s['min_retry_time'], s['max_retry_time'])
    topics = ['v1/{}/things/{}/cmd/+'.format(s['username'], s['client_id'])]
    mqtt.client.message_callback_add(topics[0], device.on_command)
    device.cayenne_mqtt = mqtt
    worker = threading.Thread(target=mqtt.start, args=(topics))
    worker.start()
    cayenne_workers.append(worker)



print("All workers started. Num cayenne client workers is %d" % len(cayenne_workers))
loc_mqtt_worker.join(0)
for w in cayenne_workers:
    w.join(0)
