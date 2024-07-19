def solution(participant, completion):
    # 1. 참가자완, 주자 리스트 정렬
    participant.sort()
    completion.sort()

    # 2. 정렬된 리스트를 순회
    for i in range(len(completion)):
		    # 일치하는 경우
        if participant[i] != completion[i]:
            # 일치하지 않는 경우
            return participant[i]

		# 완주하지 못한 마지막 참가자
    return participant[-1]
