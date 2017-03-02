# mqtt-simulator

Provides a MQTT publish and subscribe tool via docker.

```bash
docker run -d --name mosquitto -p 1883:1883 -p 9001:9001 toke/mosquitto 

docker build -t=mqtt-sim .

mon=$( docker run -d --rm --link mosquitto mqtt-sim python -u /bin/monitor.py --topic 'device/#' --host mosquitto )

docker run -t --rm --link mosquitto mqtt-sim publish.py --topic 'device/test' --host mosquitto "this is the payload"
docker run -t --rm --link mosquitto mqtt-sim publish.py --topic 'device/test' --host mosquitto "more of same"

docker logs $mon
docker logs mosquitto

docker kill $mon
docker kill mosquitto
docker rm mosquitto


```
```

```