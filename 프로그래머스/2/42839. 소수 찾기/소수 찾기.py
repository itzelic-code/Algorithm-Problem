# 순열 문제
from itertools import permutations

# 소수인지 판별하는 함수 - 에라토네스의 체
def checkPrime(n):
    if n < 2:                                 
        return False
            
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    
    return True
                   
def solution(numbers):
    answer = []
    numbers = list(numbers)
    temp = []
    
    # 문자열을 잘라서 순열로 저장 및 정수 변환
    for i in range(1, len(numbers)+1):
        temp += list(permutations(numbers, i)) 
    num = [int(''.join(t)) for t in temp] 
    
    # 소수 확인
    for i in num:
        if checkPrime(i):
            answer.append(i)
    
    return len(set(answer))