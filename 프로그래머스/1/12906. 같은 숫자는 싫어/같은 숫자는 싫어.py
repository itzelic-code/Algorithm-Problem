def solution(s):
    answer = []
    for c in s:
        if len(answer) == 0 or answer[-1] != c:
            answer.append(c)

    return answer