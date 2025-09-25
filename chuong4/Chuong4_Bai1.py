import math

print("Chương trình tính diện tích Tam Giác: - Chuong4_Bai1.py:3")
a = float(input("Nhập cạnh a>0: "))
b = float(input("Nhập cạnh b>0: "))
c = float(input("Nhập cạnh c>0: "))
if (a<=0 or b<=0 or c <=0) or (a+b)<=c or (a+c) <= b or (b+c) <= a:
    print("Tam Giác không hợp lệ! - Chuong4_Bai1.py:8")
else:
    cv = a+b+c
    p = cv /2
    dt = math.sqrt(p*(p-a) * p*(p-b) * p*(p-c))
    print("Diện tích tam giác: - Chuong4_Bai1.py:13", dt)