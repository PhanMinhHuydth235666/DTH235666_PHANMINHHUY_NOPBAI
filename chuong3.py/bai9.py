month = int(input("Nhập vào 1 tháng: "))
if month in (1, 2, 3):
    print("Tháng", month, "thuộc quý 1")
elif month in (4, 5, 6):
    print("Tháng ", month, "thuộc quý 2")
elif month in (7, 8, 9):
    print("Tháng", month, "thuộc quý 3")
elif month in (10, 11, 12):
    print("Tháng", month, "thuộc quý 4")
else:
    print("Tháng không hợp lệ")
