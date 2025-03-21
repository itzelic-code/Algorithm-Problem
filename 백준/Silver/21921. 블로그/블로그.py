import sys
input = sys.stdin.readline

N, X = map(int, input().split())
day = list(map(int, input().split()))

if max(day) == 0:
    print('SAD')
    exit(0)

value = sum(day[:X])
max_value = value
max_count = 1

# 슬라이딩 윈도우
for i in range(X, N):
    value += day[i]
    value -= day[i - X]

    if value > max_value:
        max_value = value
        max_count = 1
    elif value == max_value:
        max_count += 1

print(max_value)
print(max_count)