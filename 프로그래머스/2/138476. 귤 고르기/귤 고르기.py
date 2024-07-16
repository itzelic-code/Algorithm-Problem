def solution(k, tangerine):
    # 귤의 크기별 개수를 세기
    size_count = {}
    for size in tangerine:
        size_count[size] = size_count.get(size, 0) + 1
    
    # 크기별 개수를 내림차순으로 정렬
    sorted_size_count = sorted(size_count.values(), reverse=True)
    
    # 최소 개수의 크기를 선택하여 k개 이상 만들기
    answer = 0
    total = 0
    for count in sorted_size_count:
        total += count
        answer += 1
        if total >= k:
            break
    
    return answer