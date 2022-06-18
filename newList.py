
def singleSum(num, target):
    new_list = []
    while True:
        if sum(new_list) < target:
            new_list.append(num)
        else:
            break
    return new_list

def checkSum(lst, target):
    for ls in target:
        j = 0
        lst = []
        while j < len(lst):
            new_list = []
            i = j
            while i != len(lst):
                i += 1

l = [2, 4, 5, 7, 6]
t = 10
final_list = []

for i in l:
    lst = singleSum(i, t)
    if sum(lst) == t:
        final_list.append(lst)

print(final_list)