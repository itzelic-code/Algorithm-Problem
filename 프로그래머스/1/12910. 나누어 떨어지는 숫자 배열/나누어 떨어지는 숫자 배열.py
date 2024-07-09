def solution(arr, divisor):
    result = [num for num in arr if num % divisor == 0]
    if not result:
        return [-1]
    else:
        return sorted(result)
