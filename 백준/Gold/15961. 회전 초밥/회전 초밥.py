from sys import stdin

input = stdin.readline

n, d, k, c = map(int, input().split())  # 접시의 수, 초밥의 종류, 연속해서 먹는 접시의 수, 쿠폰 번호
sushi = [int(input()) for _ in range(n)]

kind = [0] * (d + 1)  # 초밥 종류별 카운트를 저장할 리스트
kind[c] = 1  # 쿠폰 초밥은 항상 포함되므로 미리 카운트
total_kind = 1  # 쿠폰 초밥 포함
max_kind = 0  # 최대 종류 수

# 초기 구간 설정
for i in range(k):
    if kind[sushi[i]] == 0:
        total_kind += 1
    kind[sushi[i]] += 1
max_kind = total_kind

# 투 포인터 이동
for start in range(1, n):
    end = (start + k - 1) % n
    # start-1 위치의 초밥 제거
    kind[sushi[start-1]] -= 1
    if kind[sushi[start-1]] == 0:
        total_kind -= 1
    # end 위치의 초밥 추가
    if kind[sushi[end]] == 0:
        total_kind += 1
    kind[sushi[end]] += 1
    
    max_kind = max(max_kind, total_kind)

print(max_kind)