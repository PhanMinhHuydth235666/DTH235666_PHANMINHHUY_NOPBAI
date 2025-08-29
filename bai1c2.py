import math

try:
    r = float(input("Mời bạn nhập bán kính hình tròn: "))
    cv = 2 * math.pi * r
    dt = math.pi * r ** 2
    print("Chu vi = - bai1c2.py:7", cv)
    print("Diện tích = - bai1c2.py:8", dt)
except:
    print("Lỗi rồi! - bai1c2.py:10")