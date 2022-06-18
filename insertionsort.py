a = [5, 2, 4, 6, 1, 3] # ----> 0th
# = [2, 5, 4, 6, 1, 3] # ----> 1st
# = []

def whileInsertion(a):
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j+1] = a[j]
            j = j -1
        a[j+1] = key
    return a

# def insertion(a):
#     for j in range(1, len(a)):
#         for i in range(j-1, -1, -1):
#             if a[j] < a[i]:
#                 a[i] = a[j]
#     return a

print(whileInsertion(a))
