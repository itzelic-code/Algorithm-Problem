from sys import stdin
input = stdin.readline

n = int(input())
conf =[]

for _ in range(n):
    start, end = map(int, input().split())
    conf.append((start, end))

# 회의 정렬, 끝나는 시간이 같으면 시작 시간이 빠른 순 정렬
conf.sort(key=lambda x: (x[1], x[0]))

count = 0
end_time = 0

for start, end in conf:
    if start >= end_time:
        count += 1
        end_time = end

print(count)