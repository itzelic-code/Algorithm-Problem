def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer.append(numbers[i] + numbers[j])
    
    # 중복 제거 및 오름차순 정렬
    answer = sorted(list(set(answer)))
    
    return answer
