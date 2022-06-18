def fib(n):
    # base Condition
    first = 0
    second = 1
    
    if n == 0:
        return first
    elif n == 1:
        return second
    else:
        for i in range(1, n+1):
            num = first + second
            second = first
            first = num
        return first  

print(fib(100))