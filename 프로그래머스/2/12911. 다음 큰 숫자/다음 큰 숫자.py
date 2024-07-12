def solution(n):
    # 주어진 숫자 n의 2진수 표현에서 1의 개수 구하기
    n_one_count = bin(n).count('1')
    
    # n 다음 큰 숫자 찾기
    next_num = n + 1
    while True:
        if bin(next_num).count('1') == n_one_count:
            return next_num
        next_num += 1
