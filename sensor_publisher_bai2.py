import paho.mqtt.client as mqtt
import time
import json
import random

broker = "broker.hivemq.com"
port = 1883
topic = "iot/lab/sensor01/data"

client = mqtt.Client()
client.connect(broker, port)

while True:
    temp = round(random.uniform(20.0, 40.0), 1)
    hum = round(random.uniform(30.0, 70.0), 1)
    
    data = {
        "device_id": "sensor01",
        "temperature": temp,
        "humidity": hum
    }
    
    payload = json.dumps(data)
    client.publish(topic, payload)
    print(f"Published: {payload}")
    time.sleep(3)