def fibononacci(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    return fibononacci(n - 1) + fibononacci(n-2)

print(fibononacci(7))