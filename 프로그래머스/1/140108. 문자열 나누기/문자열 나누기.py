def solution(s):
    answer, same, diff = 0, 0, 0
    for i in range(len(s)):
        if same == diff:  # 두 횟수가 같으면 answer + 1
            answer += 1
            x = s[i]
            same, diff = 0, 0
            
        if s[i] == x:
            same += 1
        else:
            diff += 1
            
    return answer