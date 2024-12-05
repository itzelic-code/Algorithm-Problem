def parenthesis_verification(s):
    stack = []
    for c in s:
        if c == '(':
            stack.append(c)
        elif c == ')':
            if not stack:
                return False
            stack.pop()
    return not stack


for _ in range(int(input())):
    target = input()
    print("YES" if parenthesis_verification(target) else "NO")
