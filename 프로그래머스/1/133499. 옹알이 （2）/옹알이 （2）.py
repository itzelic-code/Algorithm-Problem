def solution(babbling):
    answer = 0
    # 발음할 수 있는 단어 목록
    able = ["aya", "ye", "woo", "ma"]
    
    # 각 문자열에 대해 처리
    for token in babbling:
        # 발음할 수 있는 단어를 찾아 제거
        for a in able:
            # 단어가 연속으로 나오는 경우 제거하지 않음
            if a * 2 not in token:
                token = token.replace(a, ' ')
        
        # 문자열이 완전히 제거되었다면 count 증가
        if token.isspace():
            answer += 1
    
    return answer
