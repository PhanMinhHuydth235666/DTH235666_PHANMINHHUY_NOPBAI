#Câu 1:
print("\nCâu 1:\n - Chuong6.py:2")
from random import randrange

print("Chương trình xử lý List - Chuong6.py:5")
n = int(input("Nhập số phần tử: "))
lst = [0] * n

for i in range(n):
    lst[i] = randrange(-100, 100)
    
print("List ngẫu nhiên là: - Chuong6.py:12")
print(lst)

print("Mời bạn thêm số mới: - Chuong6.py:15")
value = int(input())
lst.append(value)
print(lst)

print("Bạn muốn đếm số nào: - Chuong6.py:20")
k = int(input())
dem = lst.count(k)
print(k, "xuất hiện - Chuong6.py:23", dem, "lần trong list")

def CheckPrime(n):
    d = 0
    if n <= 1:
        return False
        
    for i in range(1, n + 1):
        if n % i == 0:
            d += 1
    return d == 2

demnt = 0
tongnt = 0

for x in lst:
    if CheckPrime(x):
        demnt += 1
        tongnt += x
        
print("Có - Chuong6.py:43", demnt, "số nguyên tố trong list")
print("Tổng= - Chuong6.py:44", tongnt)

lst.sort()
print("List sau khi sort: - Chuong6.py:47")
print(lst)


del lst
print("List sau khi xóa: - Chuong6.py:52")

#Câu 2:
print("\nCâu 2:\n - Chuong6.py:55")
from random import randrange

lst = []
print("Nhập số phần tử: - Chuong6.py:59")
n = int(input())

for i in range(n):
    lst.append(randrange(0, 100))
    
print("List sau khi tạo ngẫu nhiên là: - Chuong6.py:65")
print(lst)

x = int(input("Mời bạn chèn thêm số mới: "))
lst.append(x)
print("List sau khi chèn: - Chuong6.py:70")
print(lst)

k = int(input("Mời nhập số để xóa: "))
while lst.count(k) > 0:
    lst.remove(k)
    
print("List sau khi xóa: - Chuong6.py:77")
print(lst)

def CheckDoiXung(lst):
    for i in range(len(lst)):
        if lst[i] != lst[len(lst) - i - 1]:
            return False
    return True

kt = CheckDoiXung(lst)
if kt == True:
    print("List đối xứng - Chuong6.py:88")
else:
    print("List không đối xứng - Chuong6.py:90")

#Câu 3:
print("\nCâu 3:\n - Chuong6.py:93")
from random import randrange

def TaoMaTran(m, n):
    D = []
    for i in range(m):
        row = []
        for j in range(n):
            row.append(randrange(100))
        D.append(row)
    return D

def XuatMaTran(D):
    for row in D:
        for element in row:
            print(element, end='\t - Chuong6.py:108')
        print()

def LayDong(r):
    R = D[r]
    return R

def XuatList1Chieu(R):
    for element in R:
        print(element, end='\t - Chuong6.py:117')
        
def LayCot(c):
    C = []
    for i in range(len(D)):
        C.append(D[i][c])
    return C

def MAX(D):
    max = D[0][0]
    for i in range(len(D)):
        for j in range(len(D[i])):
            if (max < D[i][j]):
                max = D[i][j]
    return max

print("Nhập số dòng: - Chuong6.py:133")
m = int(input())
print("Nhập số cột: - Chuong6.py:135")
n = int(input())

D = TaoMaTran(m, n)
XuatMaTran(D)

print("Mời bạn nhập dòng muốn xuất: - Chuong6.py:141")
r = int(input())
XuatList1Chieu(LayDong(r))

print("\nMời bạn nhập cột muốn xuất: - Chuong6.py:145")
c = int(input())
XuatList1Chieu(LayCot(c))

max = MAX(D)
print("\nSố lớn nhất trong ma trận= - Chuong6.py:150", max)

#Câu 4:
print("\nCâu 4:\n - Chuong6.py:153")
lst = [3, 0, 1, 5, 2]
x=2

print("lst[0] = - Chuong6.py:157", lst[0])
print("lst[3] = - Chuong6.py:158", lst[3])
print("lst[x] = - Chuong6.py:159", lst[x])
print("lst[x] = - Chuong6.py:160", lst[-x])
print("lst[x+1] = - Chuong6.py:161", lst[x+1])
print("lst[x] + 1= - Chuong6.py:162", lst[x] + 1)
print("lst[lst[x]] = - Chuong6.py:163", lst[lst[x]])
print("lst[lst[lst[x]]] = - Chuong6.py:164", lst[lst[lst[x]]])

#Câu 5:
print("\nCâu 5:\n - Chuong6.py:167")
lst = [20, 1, -34, 40, -8, 60, 1, 3]

print("lst = - Chuong6.py:170", lst)
print("lst[0:3] = - Chuong6.py:171", lst[0:3])
print("lst[4:8] = - Chuong6.py:172", lst[4:8])
print("lst[4:33] = - Chuong6.py:173", lst[4:33])
print("lst[5:3] = - Chuong6.py:174", lst[-5:-3])
print("lst[22:3] = - Chuong6.py:175", lst[-22:3])
print("lst[4:] = - Chuong6.py:176", lst[4:])
print("lst[:] = - Chuong6.py:177", lst[:])
print("lst[:4] = - Chuong6.py:178", lst[:4])
print("34 in lst = - Chuong6.py:179", -34 in lst)
print("34 not in lst = - Chuong6.py:180", -34 not in lst)

#Câu 6:
print("\nCâu 6:\n - Chuong6.py:183")
print("\n - Chuong6.py:184")
lst = []
n = int(input("Nhập số lượng phần tử: "))
for i in range(n):
    print("Nhập phần tử thứ - Chuong6.py:188", i +1, ": ", end="")
    so = int(input())
    lst.append(so)
    while True:
        if lst[i] in lst[0:i]:
            print("Phần tử trùng, nhập lại! - Chuong6.py:193")
            lst.remove(so)
            lst.append(int(input("Nhập phần tử thứ" + str(i + 1) + ": ")))
        else:
            break
print(lst)