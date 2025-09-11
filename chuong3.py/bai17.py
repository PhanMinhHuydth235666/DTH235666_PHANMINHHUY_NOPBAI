'''
done = False
n, m = 0, 100
while not done and n != m:
    n = int(input())
    if n < 0:
        done = True
    print("n = - bai17.py:8", n)
'''



n, m = 0, 100
while n != m:
    n = int(input())
    if n < 0:
        break
    print("n = - bai17.py:18", n)