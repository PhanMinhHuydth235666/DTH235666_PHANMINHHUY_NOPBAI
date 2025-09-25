# sum1(n): đếm từ n -> 0, trả về n (không ảnh hưởng biến global)
# sum2(): dùng global val, trả về giá trị ban đầu của val, sau đó val bị giảm về 0
# sum3(): trả về giá trị hiện tại của val (đếm từ val -> 1)
def sum1(n): 
    s = 0 
    while n > 0: 
        s += 1 
        n -= 1 
    return s 
def sum2(): 
    global val 
    s = 0 
    while val > 0: 
        s += 1 
        val -= 1 
    return s 
def sum3(): 
    s = 0 
    for i in range(val, 0, -1): 
        s += 1 
    return s

def main(): 
    global val 
    val = 5 
    print(sum1(5)) 
    print(sum2()) 
    print(sum3()) 
main()
# Trường hợp 1:
# val = 5
# sum1(5) = 5
# sum2()  = 5 (val -> 0)
# sum3()  = 0 (vì val=0)
# -> KQ: 5  5  0

def main(): 
    global val 
    val = 5 
    print(sum1(5)) 
    print(sum3()) 
    print(sum2()) 
main() 
# Trường hợp 2:
# val = 5
# sum1(5) = 5
# sum3()  = 5 (val=5)
# sum2()  = 5 (val -> 0)
# -> KQ: 5  5  5

def main(): 
    global val 
    val = 5 
    print(sum2()) 
    print(sum1(5)) 
    print(sum3()) 
main() 
# Trường hợp 3:
# val = 5
# sum2()  = 5 (val -> 0)
# sum1(5) = 5
# sum3()  = 0 (vì val=0)
# -> KQ: 5  5  0