def convert(num, n):
    if num == 0:
        return '0'

    digits = '' # n진수로 변환한 수 저장
    # num이 0이 될 때까지 n으로 나눔
    while num > 0:
        remainder = num % n
        if remainder >= 10: # 나머지가 10 이상이면 문자로 변환
            digits += chr(remainder - 10 + ord('A'))  # A, B, C...로 변환
        else:
            digits += str(remainder)
        num //= n

    return digits[::-1]  # 역순으로 반환

def solution(n, t, m, p):
    result = ''
    num = 0

    while len(result) < t * m:
        # n진수 변환
        result += convert(num, n)
        num += 1

    # 결과에서 p번째 사람의 숫자만 추출
    answer = ''
    for i in range(t):
        answer += result[p - 1 + i * m]

    return answer