def solution(n, words):
    used_words = []
    current_word = words[0][0]
    
    # words 리스트 순회
    for i, word in enumerate(words):
        # 1. 현재 단어의 첫 글자가 이전 단어의 마지막 글자와 다르거나,
        # 2. 현재 단어가 이미 사용된 단어라면
        if word[0] != current_word[-1] or word in used_words:
            # 해당 플레이어 번호 & 라운드 번호 반환
            return [(i % n) + 1, (i // n) + 1]
        
        # 리스트에 추가
        used_words.append(word)
        
        # 현재 단어 업데이트
        current_word = word
    
    # 모든 단어를 성공적으로 사용
    return [0, 0]
