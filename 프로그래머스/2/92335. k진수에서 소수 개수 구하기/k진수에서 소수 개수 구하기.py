def is_prime(num): # 소수인지 확인하는 함수
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def convert_to_k_base(n, k): # K진수로 변환하는 함수
    if n == 0:
        return '0'

    digits = ''
    while n > 0:
        digits += str(n % k)
        n //= k

    return digits[::-1]  # 역순으로 반환


def solution(n, k):
    k_base_number = convert_to_k_base(n, k)
    # 0 기준으로 분할 -> 리스트 생성
    split_numbers = k_base_number.split('0')
		
    prime_count = 0
    for number in split_numbers:
        if number:  # 빈 문자열이 아닐 경우
            decimal_number = int(number)
            if is_prime(decimal_number): # 소수이면
                prime_count += 1

    return prime_count