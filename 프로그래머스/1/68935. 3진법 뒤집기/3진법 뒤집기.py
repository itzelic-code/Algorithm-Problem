def solution(n):
    reverse = ''
    answer = 0
    # n이 0보다 클 때까지만 나누기
    while n > 0:
        # n을 3으로 나눈 나머지를 반전 3진수 reverse에 넣기
        reverse += str(n % 3)
        # n 값을 3으로 나누기
        n //= 3
    # 10진수 형태로 반환
    return int(reverse, 3)
