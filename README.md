# FLUSH-CDN-OVH
Script python to flush OVH's CDN dedicated

Go to https://api.ovh.com/createToken/index.cgi
to get your credentials

Installation
============

.. code:: bash

pip install ovh

Configure your application
============

The easiest and safest way to use your application's credentials is to create an
``ovh.conf`` configuration file in application's working directory. Here is how
it looks like:

.. code:: ini
#conf.py

application_key=my_app_key
application_secret=my_application_secret
consumer_key=my_consumer_key

serviceName =my_serverName_cdn
domain =my_domain_cdn

Run your application
============
.. code:: bash
python ClearCacheCDN.py
