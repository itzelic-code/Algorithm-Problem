import sys
input = sys.stdin.readline
n, m = map(int, input().split())
nums = list(map(int, input().split()))
sums = [0]
for num in nums:
    sums.append(sums[-1] + num)
for _ in range(m):
    i, j = map(int, input().split())
    print(sums[j] - sums[i-1])
