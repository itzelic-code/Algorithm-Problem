# 겹치는 건 싫어

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
numbers = list(map(int, input().split()))
left, right = 0, 0

counter = [0] * (max(numbers) + 1)
answer = 0

# right이 N 미만일 때까지
while right < N:
		# 만약 right가 K 미만이면 증가
    if counter[numbers[right]] < K:
        counter[numbers[right]] += 1
        right += 1
    else: # 아니면 count 감소, left 증가
        counter[numbers[left]] -= 1
        left += 1
    answer = max(answer, right - left)
print(answer)