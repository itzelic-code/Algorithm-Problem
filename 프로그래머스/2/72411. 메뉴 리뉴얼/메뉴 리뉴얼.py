from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []

    # course에 있는 각 코스 수(k)에 대해 반복
    for k in course:
        candidates = []  # 각 코스 수에 대한 후보 조합을 저장할 리스트 초기화

        # 각 주문을 순회
        for menu_li in orders:
            # 현재 주문에서 k개 메뉴의 조합을 생성
            for li in combinations(menu_li, k):
                res = ''.join(sorted(li))  # 조합을 정렬하여 문자열로 변환
                candidates.append(res)  # 후보 리스트에 추가

        # 후보 조합의 출현 빈도 계산
        sorted_candidates = Counter(candidates).most_common()  # 가장 많이 등장한 조합을 계산

        # 가장 많이 등장한 조합 중에서 등장 횟수가 1보다 크고, 가장 많이 등장한 조합과 같은 것만 선택
        answer += [menu for menu, cnt in sorted_candidates if cnt > 1 and cnt == sorted_candidates[0][1]]

    return sorted(answer)
