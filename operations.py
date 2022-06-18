def solution(operation):
    stack = []
    ans = []
    for element in operation:
        if element == 'min':
            ans.append(stack[-1])
        elif element == 'pop':
            stack.pop()
        else:
            num = int(element.split()[1])
            if stack:
                stack.append(min(stack[-1], num))
            else:
                stack.append(num)
    return ans

operations = ["push 10", "min", "push 5", "min", "push 8", "min", "pop", "min", "pop", "min"]
print(solution(operations))