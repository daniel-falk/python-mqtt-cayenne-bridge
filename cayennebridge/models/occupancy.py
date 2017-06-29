from cayennebridge.models.model import Model

class Occupancy(Model):

    def __init__(self, loc_mqtt, cayenne):
        if not 'host' in cayenne:
            raise ValueException('No cayenne host specified')
        if not 'username' in cayenne:
            raise ValueException('No cayenne username specified')
        if not 'password' in cayenne:
            raise ValueException('No cayenne password specified')
        if not 'client_id' in cayenne:
            raise ValueException('No cayenne client_id specified')

        self.loc_mqtt = loc_mqtt
        self.cayenne = cayenne

    # Register for the feed-back commands

    # For now, don't allow any correction commands from cayenne....
    def on_commad(self, client, userdata, message):
        pass
    '''
        print("A command was received: {} -> {}".format(message.topic, message.payload))
        state = message.payload.decode('utf-8').split(',')[1]
        self.loc_mqtt.client.publish(
                'commands/home/occupancy',
                payload=state,
                qos=1,
                retain=True)
    '''


    def on_change(self, client, userdata, message):
        value = int(message.payload.decode('utf-8'))
        print("Change in occupancy: {} -> {}".format(message.topic, value))
        topic = 'v1/{}/things/{}/data/0'.format(self.cayenne['username'], self.cayenne['client_id'])
        payload = 'len,m={}'.format(value)
        if not self.cayenne_mqtt is None:
            self.cayenne_mqtt.client.publish(
                    topic,
                    payload=payload,
                    qos=1,
                    retain=0) # Retained messages supported by cayenne?

