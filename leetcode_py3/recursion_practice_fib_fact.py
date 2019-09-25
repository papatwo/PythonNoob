def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return factorial(n-1) * n

print(factorial(0))

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print(fib(10))

for i in range(1000, 9999):
    if str(i*4) == str(i)[::-1]:
        return i
        