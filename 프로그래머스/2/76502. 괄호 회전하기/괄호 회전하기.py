def is_correct(s):
    stack = []
    for char in s:
        if char in "({[":
            stack.append(char)
        elif char in ")}]":
            if not stack:
                return False
            if char == ")" and stack[-1] != "(":
                return False
            if char == "}" and stack[-1] != "{":
                return False
            if char == "]" and stack[-1] != "[":
                return False
            stack.pop()
    return len(stack) == 0

def solution(s):
    count = 0
    for i in range(len(s)):
        if is_correct(s):
            count += 1
        s = s[1:] + s[0]  # 문자열을 한 칸만 회전
    return count