a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
op = input("Nhập phép toán (+, -, *, /): ")
if op == '+':
    print("Kết quả: - bai8.py:5", a + b)
elif op == '-':
    print("Kết quả: - bai8.py:7", a - b)
elif op == '*':
    print("Kết quả: - bai8.py:9", a * b)
elif op == '/':
    if b != 0:
        print("Kết quả: - bai8.py:12", a / b)
    else:
        print("Không thể chia cho 0 - bai8.py:14")
else:
    print("Phép toán không hợp lệ - bai8.py:16")