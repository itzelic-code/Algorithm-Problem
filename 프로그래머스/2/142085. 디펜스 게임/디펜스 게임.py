# 최대 힙
# 적의 공격력을 저장해서 최대 공격력을 추출

from heapq import heappop, heappush

def solution(n, k, enemy):
    answer, sumEnemy = 0, 0
    heap = []
    # 누적 공격력 계산
    for e in enemy:
        heappush(heap, -e)
        sumEnemy += e
        # 공격력이 군사 수를 초과했을 경우
        if sumEnemy > n:
            if k == 0:  # 무적권 다 썼으면 종료
                break
            # 무적권 남았으면 최대힙에서 가장 큰 적 수 처리
            sumEnemy += heappop(heap)
            k -= 1  # 무적권 사용 처리
        answer += 1
    return answer