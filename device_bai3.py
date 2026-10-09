import paho.mqtt.client as mqtt
import json

broker = "broker.hivemq.com"
port = 1883
topic_cmd = "iot/lab/light01/cmd"
topic_status = "iot/lab/light01/status"

def on_connect(client, userdata, flags, rc=None, properties=None):
    client.subscribe(topic_cmd)
    init_payload = json.dumps({
        "device_id": "light01",
        "status": "OFF"
    })
    client.publish(topic_status, init_payload)
    print(f"Da ket noi broker, gui trang thai mac dinh: {init_payload}")

def on_message(client, userdata, msg):
    command = msg.payload.decode('utf-8').strip().upper()
    if command in ["ON", "OFF"]:
        status_payload = json.dumps({
            "device_id": "light01",
            "status": command
        })
        client.publish(topic_status, status_payload)
        print(f"Nhan lenh: {command}, Da cap nhat trang thai: {status_payload}")
    else:
        print(f"Lenh khong hop le: {command}")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(broker, port)
client.loop_forever()