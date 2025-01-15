import sys
from collections import defaultdict
input = sys.stdin.readline

while True:
    # 입력
    N, K = map(int, input().split())
    if [N, K] == [0, 0]:
        break

    L = list(map(int, input().split()))  # 노드 값
    Parent = defaultdict(int)  # 부모 딕셔너리

    # 부모 탐색
    index = 0
    for i in range(1, N):
        Parent[L[i]] = L[index]  # 현재 노드의 부모를 설정

        # 다음 노드가 연속되지 않는다면 부모 인덱스를 증가시킴
        if i < N - 1 and L[i] + 1 < L[i + 1]:
            index += 1  # 부모 노드를 다음 노드로 변경

    # 조부모 탐색
    count = 0
    if Parent[Parent[K]]:  # K의 조부모가 존재하는지 확인
        for Node in L:
            # 조부모가 같고 부모가 다르면 사촌 관계이므로 카운트 증가
            if (Parent[Parent[K]] == Parent[Parent[Node]]) and Parent[Node] != Parent[K]:
                count += 1
    print(count)  # 사촌 수 출력