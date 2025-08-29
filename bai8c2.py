try:
    a = int(input("Nhập số nguyên: "))
    b = 10 / a
    print("Kết quả = - bai8c2.py:4", b)
except ZeroDivisionError:
    print("Không được chia cho 0! - bai8c2.py:6")
except ValueError:
    print("Sai kiểu dữ liệu! - bai8c2.py:8")
