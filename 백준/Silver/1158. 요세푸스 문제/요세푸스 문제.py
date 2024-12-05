N, K = map(int, input().split())
people = list(range(1, N + 1))
idx = 0
result = []

for i in range(N):
	idx = (idx + K - 1) % len(people)
	result.append(people.pop(idx))
	
print('<' + str(result)[1:-1] + '>')