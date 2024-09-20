# 단순히 한 명씩 실제로 대조하면 타임아웃
# 비율 종류 = (1:1), (2:3), (2:4), (3:4)

from collections import Counter

def solution(weights):
	answer = 0
	
	# 1:1인 경우
	counter = Counter(weights)
	for key, value in counter.items():
		if value >= 2: # 만약 동일한 무게가 중복되는 경우
			answer += value * (value - 1) // 2 # nC2
	
	weights = set(weights) # 중복 제거
	for w in weights:
		if w * 2/3 in weights: # 2:3인 경우
			answer += counter[w * 2/3] * counter[w]
		if w * 2/4 in weights: # 2:4인 경우
			answer += counter[w * 2/4] * counter[w]
		if w * 3/4 in weights: # 3:4인 경우
			answer += counter[w * 3/4] * counter[w]
			
	return answer