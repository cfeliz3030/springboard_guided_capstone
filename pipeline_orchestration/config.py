from configparser import ConfigParser

from gevent import config

config = ConfigParser()

config['postgres'] = {
    "host":'host',
        "port":'port',
        'user' : 'user',
        'password':'password',
        'database': 'database',
        'job_tracker_table_name':'name'
}


with open('config.ini','w') as configfile:
    config.write(configfile)