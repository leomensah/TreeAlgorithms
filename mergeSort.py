# Divide and conquer algorithm
# Divide the array into sections until
# they all have a length of one
# An array with a single is already sorted
# We then merge the arrays from left to right
# of the individual arrays
# from numpy import right_shift


# array = [5, 4, 3, 2, 1]
# def mergeSort(array):
#     if len(array) == 1:
#         return array
#     mid = len(array) // 2
#     left = mergeSort(array[:mid])
#     right = mergeSort(array[mid:])

    # return merge(left, right)
    # i = j = k = 0

    # while i < len(left) and j < len(right):
    #     if left[i] < right[j]:
    #         array[k] = left[i]
    #         i += 1
    #     else:
    #         array[k] = right[j]
    #         j += 1
    #     k += 1

    # # If the two arrays does not have an equal length
    # while i < len(left):
    #     array[k] = left[i]
    #     i += 1
    #     k += 1

    # while j < len(right):
    #     array[k] = right[j]
    #     j += 1
    #     k += 1
    # return merge(left, right)

# print(mergeSort(array))

# def merge(first, second):
#     length = len(first) + len(second)
#     mixed = [0] * length
#     i = j = k = 0
#     while i < len(first) and j < len(second):
#         if first[i] < second[j]:
#             mixed[k] = (first[i])
#             i += 1
#         else:
#             mixed[k] = (second[j])
#             j += 1
#         k += 1

#     # If the two arrays does not have an equal length
#     while i < len(first):
#         mixed[k] = first[i]
#         i += 1
#         k += 1

#     while j < len(second):
#         mixed[k] = second[j]
#         j += 1
#         k += 1
#     return mixed

# print(mergeSort(array))

# Divide array into two parts
# Get both parts sorted through recursion
# Merge the sorted parts.


def mergeSort(array):
    if len(array) > 1:
        mid = len(array) // 2
        left_list = array[:mid]
        right_list = array[mid:]
        mergeSort(left_list)
        mergeSort(right_list)
        merge(array, left_list, right_list)

def merge(array, left_list, right_list):
    i, j, k = 0, 0, 0
    while i<len(left_list) and j<len(right_list):
        if left_list[i] < right_list[j]:
            array[k] = left_list[i]
            i += 1
            k += 1
        else:
            array[k] = right_list[j]
            j += 1
            k += 1

    while i < len(left_list):
        array[k] = left_list[i]
        i += 1
        k += 1

    while j < len(right_list):
        array[k] = right_list[j]
        j += 1
        k += 1

array = [5, 4, 3, 2, 1]
mergeSort(array)
print(array)