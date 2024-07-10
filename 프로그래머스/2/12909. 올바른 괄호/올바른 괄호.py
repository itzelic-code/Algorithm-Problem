def solution(s):
    cnt = 0
    for char in s:
        if char == '(':
            cnt += 1
        elif char == ')':
            cnt -= 1
        if cnt < 0:
            return False
    return cnt == 0