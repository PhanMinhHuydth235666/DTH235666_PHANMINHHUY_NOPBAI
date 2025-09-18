import math

def calculate_S(x, n):
    S = 0
    for i in range(n + 1):
        exponent = 2 * i + 1
        S += (x ** exponent) / math.factorial(exponent)
    return S

# Input values
x = float(input("Enter the value of x: "))
n = int(input("Enter the value of n: "))

# Calculate the sum
result = calculate_S(x, n)

# Display the result
print(f"The value of S({x}, {n}) is: {result}")
