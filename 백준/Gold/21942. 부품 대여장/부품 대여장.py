# 부품 대여장
from collections import defaultdict
import re
import sys

# 입력값 포맷팅
input = sys.stdin.readline
n, l, f = map(str, input().rstrip().split())
n, f = int(n), int(f)
days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
l = list(map(int, re.split(r"/|:", l))) # 대여기간 분할
l = l[2] + l[1] * 60 + l[0] * 60 * 24 # 대여기간 분으로 변환

borrow = {} # 대여 명부
answer = defaultdict(int) # { 벌금 내야하는 사람 : 벌금 액수 }
for _ in range(n):
    info = input().rstrip().split()
    date = list(map(int, info[0].split('-'))) # 날짜 '-'로 분리
    time = list(map(int, info[1].split(':'))) # 시간 ':'로 분리
    object = info[2] # 대여한 물품
    name = info[3].strip() # 대여한 사람
    
    # 대여 시각과 반납 시각 분으로 변경한다.
    t = time[1] + time[0] * 60 # 분 + 시간 계산
    t += (date[2] - 1) * 24 * 60 # 일 계산
    t += 24 * 60 * sum(days[:date[1]]) # 월: 1 ~ 현재 월까지 누적합한 날짜와 비교
		
	# 처음 대여하는 경우 or 반납된 물품을 다시 대여하는 경우
    if (name, object) not in borrow or borrow[(name, object)] == -1:
        borrow[(name, object)] = t # 대여 시각 저장
    else: # 반납하는 경우
        if borrow[(name, object)] + l < t: # [반납해야하는 시각 < 반납 시각]이면 벌금
            answer[name] += (t - (borrow[(name, object)] + l)) * f # 늦은 만큼 벌금 부과
        borrow[(name, object)] = -1 # 반납 확인
            
if answer:
    answer = list(answer.items())
    answer.sort()
    for a in answer:
        print(a[0], a[1])
else:
    print(-1)
