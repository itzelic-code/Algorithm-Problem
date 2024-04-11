from collections import defaultdict
from sys import stdin
input = stdin.readline

n, d, k, c = map(int, input().split())
sushi = [int(input()) for _ in range(n)]
sushi += sushi

kind = defaultdict(int)
for i in range(k):
    kind[sushi[i]] += 1

result = len(kind)
if c not in kind:  # 쿠폰 초밥이 윈도우에 없을 때
    result += 1

for i in range(k, len(sushi)):
    kind[sushi[i]] += 1  # 새로운 초밥 추가
    kind[sushi[i-k]] -= 1  # 윈도우 밖의 초밥 삭제
    if kind[sushi[i-k]] == 0:
        del kind[sushi[i-k]]  # 카운트가 0이면 삭제
    
    current = len(kind)
    if c not in kind:  # 쿠폰 초밥이 윈도우에 없을 때
        current += 1
    result = max(result, current)  # 최대 종류 수 업데이트

print(result)