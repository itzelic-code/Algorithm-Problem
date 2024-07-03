def solution(arr):
    answer = []
    prev_num = None
    for n in arr:
        if n != prev_num:
            answer.append(n)
            prev_num = n
    return answer