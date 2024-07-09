def solution(x):
    digit_sum = sum(int(d) for d in str(x))
    return x % digit_sum == 0
