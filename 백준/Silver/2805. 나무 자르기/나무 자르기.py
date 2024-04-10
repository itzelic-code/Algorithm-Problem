from sys import stdin
input = stdin.readline

N, M = map(int, input().split())
trees = list(map(int, input().split()))

start, end = 0, max(trees)

while start <= end:
	mid = (start + end) // 2
	result = sum(tree - mid if tree > mid else 0 for tree in trees)
	
	if result < M:
		end = mid - 1
	else:
		start = mid + 1

print(end)