'''
    the result is
        There are 100 rows , 20 columns
'''

a = 0
while a<100:
    b = 0
    while b <40: 
        if (a+b) %2 == 0:
            print('* - bai14.py:11',end='')
        b +=1
    print()
    a +=1 