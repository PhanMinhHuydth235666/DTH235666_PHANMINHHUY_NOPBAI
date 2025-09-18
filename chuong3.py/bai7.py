def is_leap_year(year):
    # Năm nhuận: chia hết cho 400, hoặc chia hết cho 4 nhưng không chia hết cho 100
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)

def next_day(day, month, year):
    # Số ngày trong từng tháng
    days_in_month = [0, 31, 28 + is_leap_year(year), 31, 30, 31, 30,
                     31, 31, 30, 31, 30, 31]
    
    day += 1
    if day > days_in_month[month]:
        day = 1
        month += 1
        if month > 12:
            month = 1
            year += 1
    return day, month, year


# Nhập ngày
d = int(input("Nhập ngày: "))
m = int(input("Nhập tháng: "))
y = int(input("Nhập năm: "))

nd, nm, ny = next_day(d, m, y)
print("Ngày kế tiếp là: {}/{}/{}".format(nd, nm, ny))
