#Câu 1:
print("\n - Chuong5.py:2")

def CheckDoiXung(s):
    flag = True
    for i in range (len(s)):
        if s[i] != s [len((s)) - i -1 ]:
            flag = False
            break
    return flag

def main():
    print("Nhập 1 chuỗi: - Chuong5.py:13")
    s = input()
    if(CheckDoiXung(s)):
        print("Chuỗi đối xứng - Chuong5.py:16")
    else:
        print("Chuỗi không đối xứng - Chuong5.py:18")
while True:
    main()
    print("Tiếp tục? (c/k): - Chuong5.py:21")
    s=input()
    if s == 'k':
        break
    print("Cảm ơn - Chuong5.py:25")

#Câu 2:
print("\n - Chuong5.py:28")

def ChuoiToiUu(s):
    s2 = s
    s2 = s2.strip()
    arr=s2.split(' ')
    s2=""
    for x in arr:
        word = x
        if len(word.strip()) != 0:
            s2 = s2 + word + " "
    return s2.strip()

s = "  Trần   Duy   Thanh  "
print(s,"=> - Chuong5.py:42",len(s))
s = ChuoiToiUu(s)
print(s,"=> - Chuong5.py:44",len(s))

#Câu 3:
print("\n - Chuong5.py:47")

def CheckPrime(x):
    dem=0
    for i in range(1,x+1):
        if x % i ==0:
            dem+=1
    return dem==2
s="5;7;8;-2;8;11;-13;9;10"
arr=s.split(';')
sochan=0
soam=0
sont=0
sum=0
for x in arr:
    print(x)
    number=int(x)
    if number % 2 ==0:
        sochan+=1
    if number <0:
        soam+=1
    if CheckPrime(number):
        sont+=1
    sum=sum+number
print("Số chẵn = - Chuong5.py:71",sochan)
print("Số âm = - Chuong5.py:72",soam)
print("Số Nguyên tố = - Chuong5.py:73",sont)
print("Trung bình= - Chuong5.py:74",sum/len(arr))


#Câu 5:
print("\n - Chuong5.py:78")

s = input("Nhập vào một chuỗi: ")
chuhoa = 0
chuthuong = 0
chuso = 0
kytu = 0
khoangtrang = 0
nguyenam = 0
phuam = 0
arr = list(s)
for i in arr:
    if i >= 'A' and i <= 'Z':
        chuhoa += 1
    elif i >= 'a' and i  <='z':
        chuthuong += 1
    elif i >= '0' and i <= '9':
        chuso += 1
    elif i.isalnum():
        kytu += 1 
    elif i.isspace():
        khoangtrang += 1
    
    if (i >= 'A' and i <= 'Z') or (i >= 'a' and i  <='z'):
        if i == 'A' or i=='E' or i=='I' or i=="O" or i=="U" or i == 'a' or i=='e' or i=='i' or i=="o" or i=="u":
            nguyenam += 1
        else:
            phuam += 1

print("Tổng chữ hoa: - Chuong5.py:107", chuhoa)
print("Tổng chũ thường: - Chuong5.py:108", chuthuong)
print("Tổng chữ số: - Chuong5.py:109", chuso)
print("Tổng ký tự đặc biệt: - Chuong5.py:110", kytu)
print("Tổng khoảng trắng: - Chuong5.py:111", khoangtrang)
print("Tổng nguyên âm: - Chuong5.py:112", nguyenam)
print("Tổng phụ âm: - Chuong5.py:113", phuam)

#Câu 6:
print("\n - Chuong5.py:116")

import re

def LaySoAmTrongChuoi(c:str):
    numbers = re.findall(r'-\d+', c)
    return [int(num) for num in numbers]

c = input("Nhập chuỗi: ")
kq = LaySoAmTrongChuoi(c)
print("Các số nguyên âm trong chuỗi: - Chuong5.py:126", kq) 

#Câu 7:
print("\n - Chuong5.py:129")

def XuLyChuoi(c):
    c1 = c.title()
    c2 = c1
    c2 = c2.strip()
    arr = c2.split()
    c2 = ""
    for x in arr:
        word = x
        if len(word.strip()) != 0:
            c2 = c2 + word + " "
    return c2.strip()
c = input("Nhập vào một chuỗi: ")
print("Chuỗi sau khi xử lý: - Chuong5.py:143", XuLyChuoi(c))

#Câu 8:
print("\n - Chuong5.py:146")

def LayBaiHatCoDuoi(c):
    c1 = c.rfind("\\")
    return c[c1+1:]

def LayTenBaiHat(c):
    c1 = LayBaiHatCoDuoi(c)
    c1 = c1.split('.')
    return c1[0]

c = input("Nhập vào đường link: ")
print("Bài hát có đuôi: - Chuong5.py:158", LayBaiHatCoDuoi(c))
print("Tên bài hát: - Chuong5.py:159", LayTenBaiHat(c))