from machine import Pin, PWM
import utime

# Khởi tạo PWM cho module L9110
A_IA = PWM(Pin(3))
A_IB = PWM(Pin(2))
B_IA = PWM(Pin(5))
B_IB = PWM(Pin(4))

# Cấu hình tần số PWM
A_IA.freq(1000)
A_IB.freq(1000)
B_IA.freq(1000)
B_IB.freq(1000)

# Khởi tạo GPIO cho cảm biến IR
IR_LEFT = Pin(13, Pin.IN)
IR_CENTER = Pin(14, Pin.IN)
IR_RIGHT = Pin(15, Pin.IN)

# Hàm điều khiển động cơ với tốc độ cao
def move_forward(speed=45000):
    A_IA.duty_u16(speed)
    A_IB.duty_u16(0)
    B_IA.duty_u16(speed)
    B_IB.duty_u16(0)

def move_backward(speed=45000):
    A_IA.duty_u16(0)
    A_IB.duty_u16(speed)
    B_IA.duty_u16(0)
    B_IB.duty_u16(speed)

def turn_left_soft(speed=35000):
    A_IA.duty_u16(speed // 2)
    A_IB.duty_u16(0)
    B_IA.duty_u16(speed)
    B_IB.duty_u16(0)

def turn_left_hard(speed=45000):
    A_IA.duty_u16(0)
    A_IB.duty_u16(speed)
    B_IA.duty_u16(speed)
    B_IB.duty_u16(0)

def turn_right_soft(speed=35000):
    A_IA.duty_u16(speed)
    A_IB.duty_u16(0)
    B_IA.duty_u16(speed // 2)
    B_IB.duty_u16(0)

def turn_right_hard(speed=45000):
    A_IA.duty_u16(speed)
    A_IB.duty_u16(0)
    B_IA.duty_u16(0)
    B_IB.duty_u16(speed)

def stop():
    A_IA.duty_u16(0)
    A_IB.duty_u16(0)
    B_IA.duty_u16(0)
    B_IB.duty_u16(0)

# Vòng lặp chính
while True:
    left = IR_LEFT.value()
    center = IR_CENTER.value()
    right = IR_RIGHT.value()

    # In trạng thái cảm biến (để debug)
    print(f"Left: {left}, Center: {center}, Right: {right}")

    # Điều kiện dò line
    if center == 1 and left == 0 and right == 0:
        move_forward(45000)  # Đi thẳng nhanh
    elif center == 1 and left == 0 and right == 1:
        turn_right_hard(35000)  # Rẽ phải
    elif center == 0 and left == 0 and right == 1:
        turn_right_hard(45000)  # Rẽ phải mạnh
    elif center == 1 and left == 1 and right == 0:
        turn_left_hard(35000)  # Rẽ trái nhẹ
    elif center == 0 and left == 1 and right == 0:
        turn_left_hard(45000)  # Rẽ trái mạnh
    elif center == 0 and left == 0 and right == 0:
        move_forward(30000)  #di thang
    else:
        move_forward(45000)  # Mặc định đi thẳng

    utime.sleep(0.05)  # Giảm delay để phản hồi nhanh hơn

