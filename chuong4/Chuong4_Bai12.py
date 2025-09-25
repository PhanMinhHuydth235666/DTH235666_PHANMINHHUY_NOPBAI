def oscillate(a, b):
    for i in range(a, b):
        yield i     
        yield -i    


for n in oscillate(-3, 5):
    print(n, end=' ')
print()  

