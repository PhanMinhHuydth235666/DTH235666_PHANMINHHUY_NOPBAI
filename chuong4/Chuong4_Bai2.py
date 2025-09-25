    import random

while True:
    somay = random.randrange(1,101)
    solandoan = 0
    while solandoan < 7:
        solandoan = solandoan + 1
        songuoi = int (input("Máy đoán [1...100], mời bạn đoán: "))
        print("Bạn đoán lần thứ ", solandoan)
        if somay == songuoi:
            print("Chúc mừng bạn đoán đúng, số máy là: ", somay)
            win = True
            break
        elif somay > songuoi:
            print("Bạn đã chọn sai, số máy > số của bạn ")
        else:
            print("Bạn đã chọn sai, số máy < số của bạn ")
    if win == False:
        print("GAME OVER!, số máy: ", somay)
    hoi = input("Tiếp không(c/k)?")
    if hoi == "k":
        break
    print("Cảm ơn bạn đã chơi game ")
