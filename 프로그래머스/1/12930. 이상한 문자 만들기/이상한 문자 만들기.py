def solution(s):
    answer = ""
    w = list(s.split(" "))
    # w 안의 단어 순환
    for i in w:
        # 단어(i) (1 -> 길이) 만큼 순환
        for j in range(1, len(i)+1):
            # 짝수번째
            if j % 2 == 0:
                answer += i[j-1].lower()
            # 홀수번째
            else:
                answer += i[j-1].upper()
        answer += " "
        
    return answer[:-1]