# THỰC HÀNH PYTHON VỚI GIAO THỨC MQTT

## 1. Môi trường và Cấu hình
- **Ngôn ngữ:** Python 3.x
- **Thư viện:** `paho-mqtt` (`pip install paho-mqtt`)
- **Broker MQTT:** `broker.hivemq.com` (Port: `1883`)

---

## 2. Hướng dẫn chạy và Kết quả

### Bài 1: Gửi và nhận thông điệp MQTT cơ bản
- **Topic:** `iot/lab/message`

**Chạy chương trình:**
- Terminal 1 (Subscriber): `python subscriber_bai1.py`
- Terminal 2 (Publisher): `python publisher_bai1.py`

**Kết quả tại Subscriber:**
```text
Dang lang nghe topic: iot/lab/message
Nhan duoc message:
Topic: iot/lab/message
Payload: Xin chao tu client Python MQTT - B23DCCN028 - Le Quynh Anh
Time: 12:59:25
```

---

### Bài 2: Mô phỏng cảm biến nhiệt độ và độ ẩm
- **Topic:** `iot/lab/sensor01/data` (chu kỳ 3 giây/lần)

**Chạy chương trình:**
- Terminal 1 (Monitor): `python monitor_subscriber_bai2.py`
- Terminal 2 (Sensor): `python sensor_publisher_bai2.py`

**Kết quả tại Monitor:**
```text
Device: sensor01
Temperature: 35.8 C
Humidity: 45.4 %
CANH BAO: Nhiet do cao
--------------------
Device: sensor01
Temperature: 32.0 C
Humidity: 33.5 %
CANH BAO: Do am thap
--------------------
Device: sensor01
Temperature: 27.0 C
Humidity: 43.0 %
--------------------
```

---

### Bài 3: Điều khiển đèn thông minh
- **Topic nhận lệnh:** `iot/lab/light01/cmd`
- **Topic trạng thái:** `iot/lab/light01/status`

**Chạy chương trình:**
- Terminal 1 (Device): `python device_bai3.py`
- Terminal 2 (Controller): `python controller_bai3.py`

**Thao tác tại Controller:**
- Nhập `ON` (bật đèn) / `OFF` (tắt đèn) / `EXIT` (thoát).
- Nếu nhập lệnh sai (vd: `TEST`), controller báo lỗi và không gửi đi.

**Kết quả tại Controller:**
```text
Nhap lenh (ON/OFF) hoac EXIT de thoat: ON
Da gui lenh ON toi light01
Trang thai nhan duoc:
{"device_id": "light01", "status": "ON"}
--------------------
Nhap lenh (ON/OFF) hoac EXIT de thoat: TEST
Loi: Lenh 'TEST' khong hop le! Chi chap nhan 'ON' hoac 'OFF'.
Nhap lenh (ON/OFF) hoac EXIT de thoat: OFF
Da gui lenh OFF toi light01
Trang thai nhan duoc:
{"device_id": "light01", "status": "OFF"}
--------------------
```

**Kết quả tại Device:**
```text
Da ket noi broker, gui trang thai mac dinh: {"device_id": "light01", "status": "OFF"}
Nhan lenh: ON, Da cap nhat trang thai: {"device_id": "light01", "status": "ON"}
Nhan lenh: OFF, Da cap nhat trang thai: {"device_id": "light01", "status": "OFF"}
```