import machine
import time
import random

# Khai báo chân cảm biến siêu âm HC-SR04
TRIG = machine.Pin(1, machine.Pin.OUT)
ECHO = machine.Pin(0, machine.Pin.IN)

# Khai báo chân điều khiển động cơ (L9110S)
motorA_IA = machine.Pin(5, machine.Pin.OUT)  # Motor A (Trái) - Chân 1
motorA_IB = machine.Pin(4, machine.Pin.OUT)  # Motor A (Trái) - Chân 2
motorB_IA = machine.Pin(3, machine.Pin.OUT)  # Motor B (Phải) - Chân 1
motorB_IB = machine.Pin(2, machine.Pin.OUT)  # Motor B (Phải) - Chân 2

# Hàm đo khoảng cách
def get_distance():
    TRIG.low()
    time.sleep_us(5)
    TRIG.high()
    time.sleep_us(15)
    TRIG.low()

    pulse_time = machine.time_pulse_us(ECHO, 1, 60000)  # timeout 60ms
    if pulse_time < 0:
        return -1
    distance = (pulse_time / 2) / 29.1  # tính ra cm
    return distance

# Hàm điều khiển xe chạy thẳng
def forward():
    motorA_IA.high()
    motorA_IB.low()
    motorB_IA.high()
    motorB_IB.low()

# Hàm dừng xe
def stop():
    motorA_IA.low()
    motorA_IB.low()
    motorB_IA.low()
    motorB_IB.low()

# Hàm quay trái
def turn_left():
    motorA_IA.low()
    motorA_IB.high()  # bánh trái lùi
    motorB_IA.high()
    motorB_IB.low()   # bánh phải tiến

# Hàm quay phải
def turn_right():
    motorA_IA.high()
    motorA_IB.low()   # bánh trái tiến
    motorB_IA.low()
    motorB_IB.high()  # bánh phải lùi

# Vòng lặp chính
while True:
    distance = get_distance()
    if distance == -1:
        print("Lỗi cảm biến, không đọc được Echo")
        stop()
        time.sleep(0.5)
        continue

    print(f"Khoảng cách: {distance:.2f} cm")

    if distance < 20:  # Vật cản gần quá
        stop()
        time.sleep(0.5)

        if random.choice([True, False]):
            print("Né TRÁI")
            turn_left()
        else:
            print("Né PHẢI")
            turn_right()

        time.sleep(0.5)
        stop()
        time.sleep(0.5)

    else:
        forward()

    time.sleep(0.1)