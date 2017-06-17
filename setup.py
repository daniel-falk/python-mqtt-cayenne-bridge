from distutils.core import setup

setup(
        name = 'cayennebridge',
        version = 0.1,
        description = 'Bridge from local mqtt to cayenne cloud service',
        author = 'Daniel Falk',
        author_email = 'daniel@da-robotteknik.se',
        url = 'https://github.com/daniel-falk/python-mqtt-cayenne-bridge',
        license = 'MIT',
        install_requires = [
            'ConfigParser',
            'paho-mqtt'
            ],
        package_data = {'cayennebridge' : [
                'config.ini'
            ]},
        zip_safe = False)
