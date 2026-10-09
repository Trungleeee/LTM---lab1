import paho.mqtt.client as mqtt
import time

broker = "broker.hivemq.com"
port = 1883
topic_cmd = "iot/lab/light01/cmd"
topic_status = "iot/lab/light01/status"

def on_message(client, userdata, msg):
    print("Trang thai nhan duoc:")
    print(msg.payload.decode('utf-8'))
    print("-" * 20)

client = mqtt.Client()
client.on_message = on_message
client.connect(broker, port)
client.subscribe(topic_status)
client.loop_start()

while True:
    cmd = input("Nhap lenh (ON/OFF) hoac EXIT de thoat: ").strip().upper()
    if cmd == "EXIT":
        break
    if cmd not in ["ON", "OFF"]:
        print(f"Loi: Lenh '{cmd}' khong hop le! Chi chap nhan 'ON' hoac 'OFF'.")
        continue
    client.publish(topic_cmd, cmd)
    print(f"Da gui lenh {cmd} toi light01")
    time.sleep(1)

client.loop_stop()
client.disconnect()