# Phần 1: Hướng dẫn lắp đặt xe dò line sử dụng 2 cảm biến IR

## 🤖 Xe dò line sử dụng 2 cảm biến IR với Raspberry Pi Pico

### 📋 Danh sách linh kiện cần thiết

-   Raspberry Pi Pico (với MicroPython)
-   Module L9110 điều khiển động cơ
-   2 cảm biến IR dò line
-   2 động cơ DC
-   Pin hoặc nguồn cấp điện
-   Khung xe robot

### 🔌 Sơ đồ kết nối

-   **Cảm biến IR:**
    -   IR trái → GPIO 0
    -   IR phải → GPIO 1
-   **Module điều khiển động cơ L9110:**

    -   GND → GND
    -   VCC → 5V
    -   A-IA → GPIO 2 (PWM)
    -   A-IB → GPIO 3 (PWM)
    -   B-IA → GPIO 4 (PWM)
    -   B-IB → GPIO 5 (PWM)

-   **Động cơ DC:**
    -   Động cơ trái → A-IA, A-IB
    -   Động cơ phải → B-IA, B-IB

### 💻 Giải thích mã nguồn

Mã nguồn MicroPython được chia thành những phần chính:

1. **Khởi tạo các chân PWM** cho điều khiển động cơ
2. **Khởi tạo GPIO** cho các cảm biến IR
3. **Các hàm điều khiển chuyển động** (tiến, lùi, trái, phải, dừng)
4. **Vòng lặp chính** để đọc giá trị cảm biến và điều khiển xe

### 🧠 Nguyên lý hoạt động

-   Khi cảm biến IR **phát hiện đường line đen**, giá trị trả về là **1**
-   Khi cảm biến IR **phát hiện bề mặt trắng**, giá trị trả về là **0**
-   Xe sẽ di chuyển theo những quy tắc sau:
    -   **Cả hai cảm biến trên line (1,1)**: Đi thẳng
    -   **Cảm biến trái trên line (1,0)**: Rẽ trái
    -   **Cảm biến phải trên line (0,1)**: Rẽ phải
    -   **Không cảm biến nào trên line (0,0)**: Dừng lại

### 🔧 Tinh chỉnh và tối ưu

-   Điều chỉnh giá trị `speed` trong các hàm chuyển động để thay đổi tốc độ xe
-   Giảm giá trị `utime.sleep()` để phản ứng nhanh hơn
-   Đảo giá trị logic nếu cảm biến của bạn hoạt động ngược lại (0 khi gặp đường đen)

### 🚨 Xử lý sự cố

-   Kiểm tra pin nếu động cơ không hoạt động hoặc yếu
-   Đảm bảo cảm biến IR được đặt ở độ cao phù hợp (2-5mm) từ mặt sàn
-   Điều chỉnh độ nhạy của cảm biến IR nếu có
-   Kiểm tra kết nối dây và chân GPIO nếu xe không hoạt động như mong đợi

---

# Phần 2: Hướng dẫn cài đặt Raspberry Pi 4 với VNC và SSH

## 🚀 Hướng Dẫn Cài Đặt Raspberry Pi 4 với VNC và SSH

## 🛠️ Chuẩn Bị

Trước khi bắt đầu, bạn cần chuẩn bị:

-   💻 Máy tính cá nhân
-   💾 Thẻ nhớ SD (khuyến nghị 16GB trở lên)
-   🌐 Kết nối Internet
-   🖥️ Raspberry Pi 4

## 📥 Bước 1: Tải Phần Mềm Cần Thiết

-   📀 Tải [Raspberry Pi Imager](https://www.raspberrypi.com/software/)

![Raspberry Pi Banner](https://raw.githubusercontent.com/lehoangtrong/RaspberryPi/refs/heads/main/images/Picture1.png)
![Raspberry Pi Kit](https://raw.githubusercontent.com/lehoangtrong/RaspberryPi/refs/heads/main/images/Picture2.png)

-   🔍 Tải [RealVNC Viewer](https://www.realvnc.com/en/connect/download/viewer/)

![Raspberry Pi Imager Download](https://raw.githubusercontent.com/lehoangtrong/RaspberryPi/refs/heads/main/images/Picture3.png)
![RealVNC Viewer Download](https://raw.githubusercontent.com/lehoangtrong/RaspberryPi/refs/heads/main/images/Picture4.png)

## 💿 Bước 2: Cài Đặt Hệ Điều Hành

1. 🖱️ Mở Raspberry Pi Imager
   ![Pi Imager Interface](https://raw.githubusercontent.com/lehoangtrong/RaspberryPi/refs/heads/main/images/Picture5.png)
2. 📱 Chọn thiết bị: **Raspberry Pi 4**
   ![Selecting Device](https://raw.githubusercontent.com/lehoangtrong/RaspberryPi/refs/heads/main/images/Picture6.png)
3. 🔧 Chọn hệ điều hành phù hợp
   ![Selecting OS](https://raw.githubusercontent.com/lehoangtrong/RaspberryPi/refs/heads/main/images/Picture7.png)
4. 💾 Chọn thẻ nhớ để cài đặt
   ![Selecting Storage](https://raw.githubusercontent.com/lehoangtrong/RaspberryPi/refs/heads/main/images/Picture8.png)

## ⚙️ Bước 3: Cấu Hình Cài Đặt

1. 🖱️ Nhấn **"Edit Settings"**
   ![Edit Settings Button](https://raw.githubusercontent.com/lehoangtrong/RaspberryPi/refs/heads/main/images/Picture9.png)
2. 📝 Điền thông tin:

    - 🏠 **Hostname** (tên máy)
    - 👤 **Tên người dùng**
    - 🔑 **Mật khẩu**
    - 📶 **Thông tin WiFi**
      ![Configuration Settings](https://raw.githubusercontent.com/lehoangtrong/RaspberryPi/refs/heads/main/images/Picture10.png)

3. 🔐 Bật dịch vụ **SSH**:
    - 🔧 Chọn **"Services"**
    - ✅ Tích chọn **"Enable SSH"**
    - 🔒 Chọn **"Use password authentication"**
      ![SSH Configuration](https://raw.githubusercontent.com/lehoangtrong/RaspberryPi/refs/heads/main/images/Picture11.png)
4. 💾 Lưu cài đặt
    - 💾 Nhấn **"Save"**
    - ✍️ Nhấn **"Write"** để cài đặt hệ điều hành
    - ✅ Nhấn **"Yes"** để xác nhận
    - ⏳ Chờ quá trình cài đặt hoàn tất
      ![Saving Settings](https://raw.githubusercontent.com/lehoangtrong/RaspberryPi/refs/heads/main/images/Picture12.png)

## 📶 Bước 4: Phát WiFi Từ Máy Tính

### 🪟 Windows:

1. ⚙️ Mở **Cài Đặt (Settings)**
2. 🌐 Chọn **"Network & Internet"**
3. 📡 Chọn **"Mobile Hotspot"**
4. 🔌 Chọn kết nối Internet để chia sẻ
5. ✅ Bật **"Share my Internet connection with other devices"**
6. 🏷️ Đặt **tên mạng** và **mật khẩu**

![Windows Hotspot Setup](https://raw.githubusercontent.com/lehoangtrong/RaspberryPi/refs/heads/main/images/Picture13.png)

### 🍎 macOS:

1. ⚙️ Mở **"System Preferences"**
2. 🔄 Chọn **"Sharing"**
3. 🌐 Chọn **"Internet Sharing"**
4. 🔌 Chọn nguồn kết nối Internet
5. ✅ Tích chọn **"Wi-Fi"**
6. 🔧 Cấu hình **tên mạng** và **mật khẩu**

## 🔄 Bước 5: Kết Nối Raspberry Pi

1. 💾 Rút thẻ nhớ và gắn vào Raspberry Pi

2. 🔍 Kiểm tra kết nối WiFi:
    - 🖥️ Mở **Command Prompt (CMD)** và nhập:
        ```sh
        ping -4 raspberrypi
        ```
        ![macOS Hotspot Setup](https://raw.githubusercontent.com/lehoangtrong/RaspberryPi/refs/heads/main/images/Picture14.png)
    - 🔢 Hoặc sử dụng địa chỉ IP hiển thị khi phát WiFi
      ![Windows Hotspot Setup](https://raw.githubusercontent.com/lehoangtrong/RaspberryPi/refs/heads/main/images/Picture13.png)

## 🔐 Bước 6: Kết Nối Từ Xa (SSH)

1. 🖥️ Mở **Command Prompt**
2. ⌨️ Nhập lệnh:
    ```sh
    ssh username@ip_address
    ```
    ![SSH Command](https://raw.githubusercontent.com/lehoangtrong/RaspberryPi/refs/heads/main/images/Picture15.png)
3. 🔑 Nhập mật khẩu
    - ℹ️ Lưu ý: Gõ mật khẩu trên Linux không hiển thị ký tự khi nhập mật khẩu (không có dấu sao hoặc chấm)
    - ↩️ Sau khi nhập mật khẩu, nhấn **Enter** để xác nhận

## 🖥️ Bước 7: Cài Đặt VNC

1. 🖥️ Mở **Terminal** trên Raspberry Pi
2. ⌨️ Nhập lệnh:

    ```sh
    sudo raspi-config
    ```

    ![Raspi Config](https://raw.githubusercontent.com/lehoangtrong/RaspberryPi/refs/heads/main/images/Picture16.png)

3. 🔧 Chọn **"Interface Options"**
   ![Raspi Config](https://raw.githubusercontent.com/lehoangtrong/RaspberryPi/refs/heads/main/images/Picture17.png)

4. 🔗 Chọn **VNC**

    ![Raspi Config](https://raw.githubusercontent.com/lehoangtrong/RaspberryPi/refs/heads/main/images/Picture18.png)

5. ✅ Chọn **"Yes"** để bật VNC
   ![VNC Setup](https://raw.githubusercontent.com/lehoangtrong/RaspberryPi/refs/heads/main/images/Picture19.png)

## 🖱️ Bước 8: Truy Cập Raspberry Pi Từ Xa

1. 🔍 Mở **RealVNC Viewer**
2. 🔢 Nhập **địa chỉ IP** của Raspberry Pi
   ![RealVNC Interface](https://raw.githubusercontent.com/lehoangtrong/RaspberryPi/refs/heads/main/images/Picture20.png)
3. 🔑 Nhập **tên người dùng** và **mật khẩu**
   ![Raspberry Pi Desktop](https://raw.githubusercontent.com/lehoangtrong/RaspberryPi/refs/heads/main/images/Picture21.png)

---

## 🌐 Bước 9: Cấu Hình WiFi Qua File

Bạn cũng có thể cấu hình WiFi trực tiếp qua file `wpa_supplicant.conf`:

1. 📁 Tạo hoặc mở file `wpa_supplicant.conf`
2. 📝 Thêm nội dung sau:

```sh
country=VN
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1

network={
   ssid="Tên mạng WiFi"
   psk="Mật khẩu WiFi"
   key_mgmt=WPA-PSK
}
```

3. 💾 Lưu file và khởi động lại:

```sh
sudo reboot
```

## 🛠️ Lỗi Thường Gặp và Cách Khắc Phục

Không thể kết nối VNC với Raspberry Pi:

```sh
sudo rm /root/.vnc/private.key
sudo vncserver-x11 -generatekeys force
sudo systemctl restart vncserver-x11-serviced
```

🎉 Chúc bạn cài đặt Raspberry Pi thành công! 🚀
Nếu có bất kỳ câu hỏi nào, hãy để lại dưới đây nhé! 😊
