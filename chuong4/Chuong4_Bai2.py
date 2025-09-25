    import random

while True:
    somay = random.randrange(1,101)
    solandoan = 0
    while solandoan < 7:
        solandoan = solandoan + 1
        songuoi = int (input("Máy đoán [1...100], mời bạn đoán: "))
        print("Bạn đoán lần thứ - Chuong4_Bai2.py:9", solandoan)
        if somay == songuoi:
            print("Chúc mừng bạn đoán đúng, số máy là: - Chuong4_Bai2.py:11", somay)
            win = True
            break
        elif somay > songuoi:
            print("Bạn đã chọn sai, số máy > số của bạn - Chuong4_Bai2.py:15")
        else:
            print("Bạn đã chọn sai, số máy < số của bạn - Chuong4_Bai2.py:17")
    if win == False:
        print("GAME OVER!, số máy: - Chuong4_Bai2.py:19", somay)
    hoi = input("Tiếp không(c/k)?")
    if hoi == "k":
        break
    print("Cảm ơn bạn đã chơi game - Chuong4_Bai2.py:23")