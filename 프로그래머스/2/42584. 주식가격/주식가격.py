# 해당 문제는 스택 or 큐 자료구조로 풀이가 가능
# 스택 : 후입 선출 구조 (Last In First Out), append(), pop()
# 큐 : 선입 선출 구조 (First In First Out), append(), pop(), popleft(), appendleft()

# 큐를 사용한 풀이 방법
from collections import deque

def solution(prices):
    answer = []
    prices_q = deque(prices)
		
    while prices_q:
        price = prices_q.popleft()
        time = 0
        for q in prices_q:
            time += 1
            if price > q:
                break
        answer.append(time)
    return answer