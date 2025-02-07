n = int(input())
k = []

for _ in range(n):
    k.append(int(input()))
k.sort()

answer = []
for x in k:
    answer.append(x * n) # 최대 중량
    n -= 1
print(max(answer))