# def permutions(lst):
#     new_list = [lst]
#     for i in range(len(lst)):
#         for j in range(len(lst)):
#             for k in range(len(lst)):
#                 if not (lst[i] == lst[j] == lst[k]):
#                     new_list.append([lst[i], lst[j], lst[k]])
#     # final = []
#     # for lst in new_list:    
#     return new_list

# Break it down to how to arrange in one element
# Break it down to how to arrange it in two element
# Return the two element results to the three element
# Append the three elements results and return
# Neet Code Solution
def neetPermutations(lst):
    # Start with the base condition
    result = []
    if len(lst) == 1:
        return [lst[:]]
    for i in range(len(lst)):
        n = lst.pop(0)
        perms = neetPermutations(lst)

        for perm in perms:
            perm.append(n)
        result.extend(perms)
        lst.append(n)
    return result

print(neetPermutations([1,2,3]))