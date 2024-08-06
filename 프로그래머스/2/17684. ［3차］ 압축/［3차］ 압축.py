def solution(msg):
    answer = []
    dic = {}

    # 사전에 알파벳 추가
    for i in range(26):
        dic[chr(65 + i)] = i + 1

    w, c = 0, 0
    while True:
        c += 1  # 현재 인덱스 +1
        # 현재 인덱스가 메시지의 길이에 도달했을 때
        if c == len(msg):
            answer.append(dic[msg[w:c]])  # 마지막 인덱스를 answer에 추가
            break
        # 현재 문자열이 사전에 없는 경우
        if msg[w:c + 1] not in dic:
            dic[msg[w:c + 1]] = len(dic) + 1  # 새로운 문자열을 사전에 추가
            answer.append(dic[msg[w:c]])  # 현재 문자열 인덱스를 결과에 추가
            w = c  # 시작 인덱스를 현재 인덱스로 업데이트

    return answer