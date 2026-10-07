import paho.mqtt.client as mqtt
import json

broker = "broker.hivemq.com"
port = 1883
topic = "iot/lab/sensor01/data"

def on_message(client, userdata, msg):
    try:
        data = json.loads(msg.payload.decode('utf-8'))
        print(f"Device: {data['device_id']}")
        print(f"Temperature: {data['temperature']} C")
        print(f"Humidity: {data['humidity']} %")
        
        if data['temperature'] > 35:
            print("CANH BAO: Nhiet do cao")
        if data['humidity'] < 40:
            print("CANH BAO: Do am thap")
        print("-" * 20)
    except Exception:
        pass

client = mqtt.Client()
client.on_message = on_message
client.connect(broker, port)
client.subscribe(topic)
client.loop_forever()