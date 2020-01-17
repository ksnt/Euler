import math

def div(n):
    factors = []
    for num in range(2, int(math.sqrt(n)) + 1):
        while n % num == 0:
            n //= num 
            factors.append(num)  
    return factors

num2 = 600851475143 
print(max(div(num2)))