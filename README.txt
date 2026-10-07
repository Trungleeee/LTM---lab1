MÔI TRƯỜNG VÀ CẤU HÌNH

Ngôn ngữ: Python 3.x

Thư viện sử dụng: paho-mqtt

Lệnh cài đặt thư viện: pip install paho-mqtt

Broker MQTT sử dụng: broker.hivemq.com (Port: 1883). Đây là public broker phổ biến và ổn định cho các bài thực hành IoT.

==================================================
2. HƯỚNG DẪN CHẠY CODE VÀ KẾT QUẢ ĐẠT ĐƯỢC

LƯU Ý CHUNG: Mở các cửa sổ Terminal/Command Prompt (CMD) riêng biệt cho từng chương trình khi test để thấy rõ luồng dữ liệu publisher/subscriber.

--- Bài 1: Ứng dụng gửi và nhận thông điệp MQTT cơ bản ---

Bước 1: Mở Terminal thứ nhất, chạy file Subscriber:

python subscriber_bai1.py
(Chương trình sẽ hiển thị "Dang lang nghe topic: iot/lab/message")

Bước 2: Mở Terminal thứ hai, chạy file Publisher:

python publisher_bai1.py
(Chương trình sẽ tự động gửi message mỗi 5 giây với nội dung chứa tên Lê Quỳnh Anh)

Kết quả: Ở Terminal 1 (subscriber), bạn sẽ thấy các block thông điệp được in ra rõ ràng với Topic, Payload, và Thời gian nhận.

--- Bài 2: Mô phỏng cảm biến nhiệt độ và độ ẩm ---

Bước 1: Mở Terminal thứ nhất, chạy file Monitor:

python monitor_subscriber_bai2.py

Bước 2: Mở Terminal thứ hai, chạy file Sensor:

python sensor_publisher_bai2.py
(Cảm biến sẽ sinh ngẫu nhiên số liệu và đẩy định dạng JSON mỗi 3 giây)

Kết quả: Monitor sẽ parse chuỗi JSON, trích xuất dữ liệu in ra màn hình. Nếu nhiệt độ > 35 hoặc độ ẩm < 40, hệ thống sẽ in ra dòng cảnh báo "CANH BAO".

--- Bài 3: Mô phỏng hệ thống điều khiển đèn thông minh ---

Bước 1: Mở Terminal thứ nhất, khởi động thiết bị đèn:

python device_bai3.py
(Đèn sẽ báo kết nối và publish trạng thái mặc định là OFF lên status)

Bước 2: Mở Terminal thứ hai, khởi động Controller:

python controller_bai3.py

Bước 3: Trong Terminal của Controller, thử nhập các lệnh "ON", sau đó là "OFF".

Kết quả: Controller publish lệnh đi, Device nhận được sẽ chuyển trạng thái và gửi phản hồi dạng JSON {"device_id": "light01", "status": "ON"}. Controller lắng nghe phản hồi này và in trực tiếp ra màn hình ngay khi đèn bật/tắt.
Nếu nhập lệnh sai (vd: "TEST"), controller sẽ chặn lại. Nhập "EXIT" để thoát.