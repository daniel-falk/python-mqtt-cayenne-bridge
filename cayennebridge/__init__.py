from configparser import ConfigParser, NoOptionError
from pkg_resources import resource_filename
from os import path

from cayennebridge.mqtt import Mqtt


# Read config file
GLOBAL_CONF = '/etc/cayennebridge/config.ini'

if path.isfile(GLOBAL_CONF):
    f = GLOBAL_CONF
else:
    f = resource_filename('cayennebridge', 'config.ini')

conf = ConfigParser()
conf.read(f)


# Connect to the local mqtt network

server = conf.get('LOCAL', 'host')
try:
    username = conf.get('LOCAL', 'username')
except NoOptionError:
    username = None
try:
    password = conf.get('LOCAL', 'password')
except NoOptionError:
    password = None
try:
    client_id = conf.get('LOCAL', 'client_id')
except NoOptionError:
    client_id = 'CAYENNE_BRIDGE_CLIENT'
try:
    keepalive = int(conf.get('LOCAL', 'keepalive'))
except NoOptionError:
    keepalive = 30
try:
    min_retry_time = int(conf.get('LOCAL', 'min_retry_time'))
except NoOptionError:
    min_retry_time = 2
try:
    max_retry_time = int(conf.get('LOCAL', 'max_retry_time'))
except NoOptionError:
    max_retry_time = 60

loc_mqtt = Mqtt('Local MQTT', server, username, password, client_id, keepalive, min_retry_time, max_retry_time)
