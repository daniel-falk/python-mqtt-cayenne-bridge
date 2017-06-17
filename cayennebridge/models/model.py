
class Model(object):
    loc_mqtt = None
    cayenne_mqtt = None
    local_topics = []

    cayenne = {
            'keepalive':60,
            'min_retry_time':10,
            'max_retry_time':600}

    def on_command(self, userdata, message):
        raise Exception('Not implemented')
