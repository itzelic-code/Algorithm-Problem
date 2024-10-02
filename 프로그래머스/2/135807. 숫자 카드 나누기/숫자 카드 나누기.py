from math import gcd

def solution(arrayA, arrayB):
    a = arrayA[0]
    b = arrayB[0]
		
		# 각 배열의 최대공약수 설정
    for i in range(len(arrayA)):
        a = gcd(a, arrayA[i])
        b = gcd(b, arrayB[i])
		
		# 두 조건 판별
    A_iszero = 1
    B_iszero = 1
    for i in range(len(arrayA)):
        if arrayA[i] % b == 0:
            A_iszero = 0
        if arrayB[i] % a == 0:
            B_iszero = 0
		
		# 조건을 만족하는 a가 없다면 0 반환
    if A_iszero == 0 and B_iszero == 0:
        return 0
    else:
        return max(a, b)