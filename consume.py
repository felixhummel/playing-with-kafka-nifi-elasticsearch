#!/usr/bin/env python
# encoding: utf-8
"""
https://github.com/dpkp/kafka-python
"""

import json
import dateutil.parser
import time

from kafka import KafkaConsumer


TOPIC = 'foo'
consumer = KafkaConsumer(TOPIC)


def main():
    for record in consumer:
        thing = json.loads(str(record.value, encoding='utf-8'))
        dt = dateutil.parser.parse(thing['date'])
        print(dt, thing['action'])


if __name__ == '__main__':
    main()
