def solution(n):
    answer = ''

    while n > 0:
        n -= 1
        remain = n % 3
        if remain == 0:
            answer = '1' + answer
        elif remain == 1:
            answer = '2' + answer
        else: # 2
            answer = '4' + answer
        n //= 3
    return answer