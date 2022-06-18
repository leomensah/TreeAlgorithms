def climbing_stairs(lst):
    one, two = 1, 1
    for i in range(lst-1):
        temp = one
        one = one + two
        two = temp
    return one

print(climbing_stairs(5))