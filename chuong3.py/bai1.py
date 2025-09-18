print("Chương trình kiểm tra năm nhuận - bai1.py:1")
year = int(input("Mời bạn nhập vào 1 năm: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Năm ", year, "là năm nhuận")
else:
    print("Năm ", year, "không nhuận")
