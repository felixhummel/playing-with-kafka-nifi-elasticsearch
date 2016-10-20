#!/usr/bin/env python
# encoding: utf-8
"""
https://github.com/dpkp/kafka-python
"""

import json
import datetime
import pytz
import random
import uuid
import time

from kafka import KafkaProducer


TOPIC = 'foo'
producer = KafkaProducer()


def send(thing):
    producer.send(TOPIC, bytes(json.dumps(thing), 'utf-8'))


def while_true():
    sleep_times = [0.3, 0.4, 0.5, 0.6, 0.7, 0.8]
    actions = ['foo', 'bar', 'baz']
    groups = [1, 2, 3, 4, 5]
    while True:
        payload = {
                'id': str(uuid.uuid4()),
                'action': random.choice(actions),
                'group': random.choice(groups),
                'date': datetime.datetime.now(pytz.timezone('Europe/Berlin'))
                            .isoformat(),
        }
        send(payload)
        producer.flush()
        sleep_seconds = random.choice(sleep_times)
        print("{0} [sleeping {1}]".format(payload, sleep_seconds))
        time.sleep(random.choice(sleep_times))


if __name__ == '__main__':
    while_true()
