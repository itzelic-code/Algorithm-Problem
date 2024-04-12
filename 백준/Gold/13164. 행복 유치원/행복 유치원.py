from sys import stdin
input = stdin.readline

n, k = map(int, input().split())
height = list(map(int, input().split()))

difference = []
for i in range(1, n):
    difference.append(height[i] - height[i-1])
difference.sort(reverse=True)

print(sum(difference[k-1:]))