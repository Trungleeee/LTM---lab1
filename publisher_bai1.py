import paho.mqtt.client as mqtt
import time

broker = "broker.hivemq.com"
port = 1883
topic = "iot/lab/message"

client = mqtt.Client()
client.connect(broker, port)

ho_ten = "Lê Quỳnh Anh"
msv = "B23DCCN028"
loi_chao = "Xin chao tu client Python MQTT"
payload = f"{loi_chao} - {msv} - {ho_ten}"

while True:
    client.publish(topic, payload)
    print(f"Da gui message: {payload}")
    time.sleep(5)