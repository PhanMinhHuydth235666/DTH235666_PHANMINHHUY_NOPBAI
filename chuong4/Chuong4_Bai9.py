import math

def TinhS(n):
    if n == 1:
        return math.sqrt(2)
    else:
        return math.sqrt(2 + TinhS(n-1))

n = int(input("Nhập n: "))
print("S(n) = ", TinhS(n))
