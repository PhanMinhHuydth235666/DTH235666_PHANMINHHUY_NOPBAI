print("Chương trình đếm số ngày trong tháng - bai2.py:1")
month = int(input("Nhập vào 1 tháng: "))
if month in (1, 3, 5, 7, 8, 10, 12):
    print("Tháng - bai2.py:4", month, "có 31 ngày")
elif month in (4, 6, 9, 11):
    print("Tháng - bai2.py:6", month, "có 30 ngày")
elif month == 2:
    year = int(input("Mời bạn nhập vào năm: "))
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("Tháng - bai2.py:10", month, "có 29 ngày")
    else:
        print("Tháng - bai2.py:12", month, "có 28 ngày")
else:
    print("Tháng - bai2.py:14", month, "không hợp lệ")