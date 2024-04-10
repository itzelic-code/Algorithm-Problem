"""
* 메모리 : 31252KB
* 시간 : 44ms
* 사용된 개념 : 이진 탐색
--------------------------------------------------
* 접근 방법
1. 나무 수 N, 나무 길이 M 입력
2. 나무의 높이를 리스트에 저장
3. 나무 높이 최소값, 최대값 설정.
4. 이진탐색 - 잘라 가져갈 수 있는 최대 높이 찾기.
	4-1. mid(나무 자르는 높이)로 잘랐을때 얻는 나무 길이 계산
5. 잘라낸 나무 총 길이가 필요한 길이 이상이면,
	5-1. 더 많은 나무를 얻기 위해 mid값 높이기(left 조정)
	5-2. 그렇지 않으면 mid값 낮추기 (right 조정)
6. 나무를 자르는 최대 높이 출력
--------------------------------------------------

"""
from sys import stdin
input = stdin.readline

N, M = map(int, input().split())
tree = list(map(int, input().split()))

left, right = 0, max(tree)

while left <= right:
    mid = (left + right) // 2  # 현재 높이
    cut = sum(t - mid if t > mid else 0 for t in tree)  # 잘린 나무 총 길이
    
    if cut >= M:  # 잘린 나무 길이가 필요한 길이보다 많을 때
        left = mid + 1  # left 조정
    else:  # 잘린 나무 길이가 부족할 때
        right = mid - 1  # right 조정

print(right)