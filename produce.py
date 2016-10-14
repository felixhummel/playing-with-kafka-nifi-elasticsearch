#!/usr/bin/env python
# encoding: utf-8
"""
https://github.com/dpkp/kafka-python
"""

import json
import datetime
import pytz
import uuid
import time

from kafka import KafkaProducer


TOPIC = 'foo'
producer = KafkaProducer()


def send(thing):
    producer.send(TOPIC, bytes(json.dumps(thing), 'utf-8'))


def while_true(sleep_s=0.5, actions=None):
    if actions is None:
        actions = ['foo', 'bar', 'baz']
    while True:
        for action in actions:
            dt = datetime.datetime.now(pytz.timezone('Europe/Berlin')).isoformat()
            payload = {'action': action, 'date': dt, 'id': str(uuid.uuid4())}
            print(payload)
            send(payload)
        producer.flush()
        time.sleep(sleep_s)


if __name__ == '__main__':
    while_true()
