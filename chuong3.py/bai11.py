while True:
    n = int(input("Nhập 1 số nguyên dương: "))
    dem = 0
    for i in range(1, n+1):
        if n % i == 0:
            dem += 1
    if dem == 2:
        print(n, "Là số nguyên tố - bai11.py:8")
    else:
        print(n, "Không là số nguyên tố - bai11.py:10")
    hoi = input("Tiếp không Thím? (c/k): ")
    if hoi == "k":
        break
print("BYE! - bai11.py:14")