import math
def DoDai(xA, yA, xB, yB):
    return math.sqrt((xB - xA)**2 + (yB - yA)**2)

print("Chương trình tính độ dài đoạn AB ")
print("Nhập điểm A(x,y): ")
xA = float(input("Nhập xA: "))
yA = float(input("Nhập yA: "))

print("Nhập điểm B(x,y): ")
xB = float(input("Nhập xB: "))
yB = float(input("Nhập yB: "))

print("Độ dài cạnh |AB| = ", DoDai(xA,  yA, xB, yB))
