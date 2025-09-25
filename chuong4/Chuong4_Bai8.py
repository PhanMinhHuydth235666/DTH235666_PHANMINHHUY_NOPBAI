import math

def TinhLog(x, a):
    return math.log(x) / math.log(a)

while True:
    x = float(input("Nhập x: "))
    if(x <= 0):
        print("x phải >0. Nhập lại - Chuong4_Bai8.py:9")
    else:
        break

while True:
    a = float(input("Nhập a: "))
    if(a <= 0 and a != 0):
        print("a phải >0 và a != 0. Nhập lại - Chuong4_Bai8.py:16")
    else:
        break

print("Kết quả (loga)^x = - Chuong4_Bai8.py:20", TinhLog(x, a))