import math

def TinhS(n):
    if n == 1:
        return math.sqrt(2)
    else:
        return math.sqrt(2 + TinhS(n-1))

n = int(input("Nhập n: "))
print("S(n) = - Chuong4_Bai9.py:10", TinhS(n))