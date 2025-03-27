# 🍓 Hướng Dẫn Cài Đặt Raspberry Pi Đơn Giản

## 🛠️ Chuẩn Bị

Trước khi bắt đầu, bạn cần chuẩn bị:
- 💻 Máy tính cá nhân
- 💾 Thẻ nhớ SD (khuyến nghị 16GB trở lên)
- 🌐 Kết nối Internet
- 🖥️ Raspberry Pi 4

## 📥 Bước 1: Tải Phần Mềm Cần Thiết

- 📀 Tải [Raspberry Pi Imager](https://www.raspberrypi.com/software/)

![Raspberry Pi Banner](images/picture1.png)
![Raspberry Pi Kit](images/picture2.png)

- 🔍 Tải [RealVNC Viewer](https://www.realvnc.com/en/connect/download/viewer/)

![Raspberry Pi Imager Download](images/picture3.png)
![RealVNC Viewer Download](images/picture4.png)

## 💿 Bước 2: Cài Đặt Hệ Điều Hành

1. 🖱️ Mở Raspberry Pi Imager
![Pi Imager Interface](images/picture5.png)
2. 📱 Chọn thiết bị: **Raspberry Pi 4**
![Selecting Device](images/picture6.png)
3. 🔧 Chọn hệ điều hành phù hợp
![Selecting OS](images/picture7.png)
4. 💾 Chọn thẻ nhớ để cài đặt
![Selecting Storage](images/picture8.png)

## ⚙️ Bước 3: Cấu Hình Cài Đặt

1. 🖱️ Nhấn **"Edit Settings"**
![Edit Settings Button](images/picture9.png)
2. 📝 Điền thông tin:
   - 🏠 **Hostname** (tên máy)
   - 👤 **Tên người dùng**
   - 🔑 **Mật khẩu**
   - 📶 **Thông tin WiFi**
![Configuration Settings](images/picture10.png)

3. 🔐 Bật dịch vụ **SSH**:
   - 🔧 Chọn **"Services"**
   - ✅ Tích chọn **"Enable SSH"**
   - 🔒 Chọn **"Use password authentication"**
![SSH Configuration](images/picture11.png)
4. 💾 Lưu cài đặt
   - 💾 Nhấn **"Save"**
   - ✍️ Nhấn **"Write"** để cài đặt hệ điều hành
   - ✅ Nhấn **"Yes"** để xác nhận
   - ⏳ Chờ quá trình cài đặt hoàn tất
![Saving Settings](images/picture12.png)

## 📶 Bước 4: Phát WiFi Từ Máy Tính

### 🪟 Windows:
1. ⚙️ Mở **Cài Đặt (Settings)**
2. 🌐 Chọn **"Network & Internet"**
3. 📡 Chọn **"Mobile Hotspot"**
4. 🔌 Chọn kết nối Internet để chia sẻ
5. ✅ Bật **"Share my Internet connection with other devices"**
6. 🏷️ Đặt **tên mạng** và **mật khẩu**

![Windows Hotspot Setup](images/picture13.png)

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
     ![macOS Hotspot Setup](images/picture14.png)
   - 🔢 Hoặc sử dụng địa chỉ IP hiển thị khi phát WiFi
   ![Windows Hotspot Setup](images/picture13.png) 

## 🔐 Bước 6: Kết Nối Từ Xa (SSH)

1. 🖥️ Mở **Command Prompt**
2. ⌨️ Nhập lệnh:
   ```sh
   ssh username@ip_address
   ```
   ![SSH Command](images/picture15.png)
3. 🔑 Nhập mật khẩu
   - ℹ️ Lưu ý: Gõ mật khẩu trên Linux không hiển thị ký tự khi nhập mật khẩu (không có dấu sao hoặc chấm)
   - ↩️ Sau khi nhập mật khẩu, nhấn **Enter** để xác nhận

## 🖥️ Bước 7: Cài Đặt VNC

1. 🖥️ Mở **Terminal** trên Raspberry Pi
2. ⌨️ Nhập lệnh:
   ```sh
   sudo raspi-config
   ```
   ![Raspi Config](images/picture16.png)
3. 🔧 Chọn **"Interface Options"**
   ![Raspi Config](images/picture17.png)
4. 🔗 Chọn **VNC**
   ![Raspi Config](images/picture18.png)

5. ✅ Chọn **"Yes"**
   ![VNC Setup](images/picture19.png)

## 🖱️ Bước 8: Truy Cập Raspberry Pi Từ Xa

1. 🔍 Mở **RealVNC Viewer**
2. 🔢 Nhập **địa chỉ IP** của Raspberry Pi
   ![RealVNC Interface](images/picture20.png)
3. 🔑 Nhập **tên người dùng** và **mật khẩu**
   ![Raspberry Pi Desktop](images/picture21.png)

---

🎉 Chúc bạn cài đặt Raspberry Pi thành công! 🚀