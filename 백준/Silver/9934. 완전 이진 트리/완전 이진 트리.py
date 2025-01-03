def reverse_inorder(start, end, level):
    if start == end:
        # 현재 구간에 하나의 노드만 남아있는 경우 (리프 노드)
        answer[level].append(tree[start])  # 해당 노드를 현재 레벨에 추가
        return  # 재귀 종료
    
    # 현재 구간의 중앙 인덱스를 계산하여 루트 노드로 선정
    center = (start + end) // 2
    answer[level].append(tree[center])  # 중앙 노드를 현재 레벨에 추가
    
    # 왼쪽 서브트리 처리: start부터 center-1까지
    reverse_inorder(start, center - 1, level + 1)
    
    # 오른쪽 서브트리 처리: center+1부터 end까지
    reverse_inorder(center + 1, end, level + 1)


# 트리의 레벨 수 입력 받기
level = int(input())
tree = list(map(int, input().split()))
l = len(tree)
answer = [[] for _ in range(level)]

# 전체 배열을 대상으로 트리 생성
reverse_inorder(0, l - 1, 0)

# 출력
for a in answer:
    print(*a)