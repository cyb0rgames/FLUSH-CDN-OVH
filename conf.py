#!/usr/bin/python
import ovh

client = ovh.Client(
    endpoint='ovh-eu',
    application_key=my_app_key
    application_secret=my_application_secret
    consumer_key=my_consumer_key
)

serviceName =my_serverName_cdn
domain =my_domain_cdn
