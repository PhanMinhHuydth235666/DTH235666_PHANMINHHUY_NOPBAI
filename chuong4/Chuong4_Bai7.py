import math
def DoDai(xA, yA, xB, yB):
    return math.sqrt((xB - xA)**2 + (yB - yA)**2)

print("Chương trình tính độ dài đoạn AB - Chuong4_Bai7.py:5")
print("Nhập điểm A(x,y): - Chuong4_Bai7.py:6")
xA = float(input("Nhập xA: "))
yA = float(input("Nhập yA: "))

print("Nhập điểm B(x,y): - Chuong4_Bai7.py:10")
xB = float(input("Nhập xB: "))
yB = float(input("Nhập yB: "))

print("Độ dài cạnh |AB| = - Chuong4_Bai7.py:14", DoDai(xA,  yA, xB, yB))