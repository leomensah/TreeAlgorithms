def solution(a):
    stack = []
    res = [-1] * len(a)
    for i, el in enumerate(a):
        while stack and a[stack[- 1]] < el:
            res[stack[- 1]] = el
            stack.pop()
        stack.append(i)
    return res


a = [6, 7, 3, 8]
b = [1, 3, 2, 4]
print(solution(a))
print(solution(b))