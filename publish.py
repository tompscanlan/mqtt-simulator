#!/usr/bin/env python

import argparse
import paho.mqtt.publish as publish


parser = argparse.ArgumentParser(description='simple iot mqqt publisher')


parser.add_argument('payload', default='payload',
                    help='payload contents')
parser.add_argument('--topic', default='devices/test',
                    help='name of topic to monitor')
parser.add_argument('--host', default='localhost',
                    help='hostname of mqtt broker')
parser.add_argument('-p', '--port', metavar='port', default=1883,
                    help='mqtt broker port number')
args = parser.parse_args()



#publish.single("paho/test/single", "payload", hostname="iot.eclipse.org")
publish.single(args.topic, str(args.payload), hostname=args.host, port=args.port)
