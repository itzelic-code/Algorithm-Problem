from sys import stdin
input = stdin.readline

n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]
lines.sort()

# LIS 찾기
dp = [1] * n  # LIS의 길이
for i in range(n):
    for j in range(i):
        if lines[i][1] > lines[j][1]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))