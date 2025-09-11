

n = 4
# Square: 0 -> n-1 = n -1
for i in range(n):
    result = ''
    for j in range(n):
        if(i == 0 or i == n -1):
            result += "*"
        else:
            if(j == 0 or j == n-1):
                result += "*"
            else:
                result += " "
    
    print(result)
print()   
#Triangle
# 
#               

n2 = 4
result  = ''
for i in range(n2):
    result = " "*(n2 - i -1) + "*"*(i +1)
    print(result)


print()
#... n = 7

m = 7
mid = m // 2
for i in range(m):
    result = ''
    for j in range(m):
            if i == j or (j == 0 and i < mid) or (j == m-1 and i >= mid) :
                result += "*"
            elif mid == i:
                result += "*"
            else:
                result += " "  

    print(result)


'''
I divide the image into 2 parts: the front and the rear

    with the front: j == 0    is "*"
    with the rear : j == m-1  is "*"

I see i == j and mid == i are "*" and the remaining ones are " "
'''