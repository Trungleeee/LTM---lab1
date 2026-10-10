import paho.mqtt.client as mqtt
import datetime

broker = "broker.hivemq.com"
port = 1883
topic = "iot/lab/message"

def on_message(client, userdata, msg):
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    print("Nhan duoc message:")
    print(f"Topic: {msg.topic}")
    print(f"Payload: {msg.payload.decode('utf-8')}")
    print(f"Time: {current_time}\n")

client = mqtt.Client()
client.on_message = on_message
client.connect(broker, port)
client.subscribe(topic)
print(f"Dang lang nghe topic: {topic}")
client.loop_forever()