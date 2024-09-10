def solution(numbers, k):
    stack = []
    for num in numbers:
        while k > 0 and stack and stack[-1] < num:
            stack.pop()
            k -= 1
        stack.append(num)
    if k > 0:
        stack = stack[:-k]
    return ''.join(stack)