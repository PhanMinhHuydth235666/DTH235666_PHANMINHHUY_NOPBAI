from math import sqrt
print("Chương trình Giải Phương trình bậc 2 - bai3.py:2")
a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
c = float(input("Nhập c: "))
if a == 0:
    if b == 0 and c == 0:
        print("Vô số nghiệm - bai3.py:8")
    elif b == 0 and c != 0:
        print("Vô nghiệm - bai3.py:10")
    else:
        x = -c / b
        print("Nghiệm x = - bai3.py:13", x)
else:
    delta = b**2 - 4*a*c
    if delta < 0:
        print("Vô nghiệm - bai3.py:17")
    elif delta == 0:
        x = -b / (2*a)
        print("Nghiệm kép x1 = x2 = - bai3.py:20", x)
    else:
        x1 = (-b - sqrt(delta)) / (2*a)
        x2 = (-b + sqrt(delta)) / (2*a)
        print("x1 = ", x1)
        print("x2 = ", x2)
