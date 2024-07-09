def solution(n):
    answer = []
    for digit in str(n)[::-1]:
        answer.append(int(digit))
    return answer