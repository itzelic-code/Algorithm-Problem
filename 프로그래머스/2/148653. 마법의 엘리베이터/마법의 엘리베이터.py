def solution(storey):
	answer = 0
	
	while storey:
		remainder = storey % 10
		# 5 < 현재 값 < 10
		if remainder > 5:
			answer += (10 - remainder)
			storey += 10
		# 0 < 현재 값 < 5
		elif remainder < 5:
			answer += remainder
		else: # 현재 값 = 5
			if (storey // 10) % 10 > 4:
				storey += 10
			answer += remainder
		storey //= 10
		
	return answer