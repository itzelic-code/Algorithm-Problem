from itertools import combinations


# 소수 판별하는 함수
def is_prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def solution(nums):
    answer = 0
    for i in combinations(nums, 3):
        if is_prime(sum(i)):
            answer += 1
    return answer