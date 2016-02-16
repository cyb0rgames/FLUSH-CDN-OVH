#!/usr/bin/python

import conf

conf.client.post('/cdn/dedicated/%s/domains/%s/flush' %(conf.serviceName, conf.domain))

tasks = conf.client.get('/cdn/dedicated/%s/domains/%s/tasks' %(conf.serviceName, conf.domain))

for task in tasks:
    details = conf.client.get('/cdn/dedicated/%s/domains/%s/tasks/%s' %(conf.serviceName, conf.domain, task))
    print details
