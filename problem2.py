from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n < 3:
         return n
    return fib(n-1) + fib(n-2)

i = 2
result = 0
while True:
    fib_num = fib(i)
    if fib_num <= 4000000:
        result = result + fib_num
        i = i + 3
        #print(fib_num)
    else:
        break

print(result)