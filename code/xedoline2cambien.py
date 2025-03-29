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

# Hàm điều khiển động cơ

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


def turn_left(speed=35000):
    A_IA.duty_u16(0)
    A_IB.duty_u16(speed)
    B_IA.duty_u16(speed)
    B_IB.duty_u16(0)


def turn_right(speed=35000):
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
    right = IR_RIGHT.value()

    # In trạng thái cảm biến (để debug)
    print(f"Left: {left}, Right: {right}")

    # Điều kiện dò line với 2 cảm biến
    if left == 1 and right == 1: 
        move_forward(45000)  # Cả hai cảm biến đều trên line đen, đi thẳng nhanh
    elif left == 1 and right == 0:
        turn_left(45000)  # Cảm biến trái thấy line đen, rẽ trái
    elif left == 0 and right == 1:
        turn_right(45000)  # Cảm biến phải thấy line đen, rẽ phải
    else:
        stop()  # Nếu cả hai cảm biến không thấy line, dừng lại


    utime.sleep(0.05)  # Giảm delay để phản hồi nhanh hơn