from cayennebridge.models.model import Model

class HallLight(Model):

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
        self.cayenne.update(cayenne)

        # Register for the feed-back commands


    def on_command(self, client, userdata, message):
        print("A command was received: {} -> {}".format(message.topic, message.payload))
        state = message.payload.decode('utf-8').split(',')[1]
        self.loc_mqtt.client.publish(
                'commands/hall/set/roof',
                payload='on' if state=='1' else 'off',
                qos=1,
                retain=False)


    def on_command_res(self, client, userdata, message):
        print("A command result was received: {} -> {}".format(message.topic, message.payload))
        state = message.payload.decode('utf-8').split(',')[1]
        if not self.cayenne_mqtt is None:
            self.cayenne_mqtt.client.publish(
                    'v1/{}/things/{}/data/0'.format(self.cayenne['username'], self.cayenne['client_id']),
                    payload='1' if state=='on' else '0',
                    qos=1,
                    retain=0)

