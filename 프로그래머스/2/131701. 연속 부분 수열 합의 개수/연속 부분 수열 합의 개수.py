def solution(elements):
    n = len(elements)
    unique_sums = set()
    # 원형 배열로 변경
    extended_elements = elements * 2

    # 모든 연속 부분 수열 순회
    for length in range(1, n + 1): # 부분 수열 길이
        for start in range(n):  # 시작 인덱스
            current_sum = sum(extended_elements[start:start + length])
            unique_sums.add(current_sum)

    return len(unique_sums)
