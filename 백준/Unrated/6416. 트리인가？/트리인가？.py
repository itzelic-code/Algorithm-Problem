from collections import deque
import sys

rl = sys.stdin.readline
caseCnt = 0
Lines = dict()

class Node:
    def __init__(self, item: int):
        self.item = item
        self.canGoTo = []
        self.canComeFrom = []
        self.canFromRoot = False

class Tree:
    def __init__(self, root: Node):
        self.root = root

    def levelorder(self, n: Node):
        if n is not None:
            queue = deque()
            queue.append(n)
            while queue:
                tmp = queue.popleft()
                if not tmp.canFromRoot:
                    tmp.canFromRoot = True
                    for item in tmp.canGoTo:
                        queue.append(nodes[item])

while True:
    INP = rl().rstrip()
    if INP == '-1 -1':  # 입력 종료
        break
    elif INP == '':  # 빈 줄 무시
        continue

    caseEnd = 0
    inputLine = list(map(int, INP.split()))
    for i in range(0, len(inputLine), 2):
        if inputLine[i] == 0 and inputLine[i+1] == 0:  # 케이스 입력 종료
            caseEnd = 1
            break
        elif inputLine[i] in Lines:  # 출발점이 이미 존재하는 경우
            Lines[inputLine[i]].append(inputLine[i+1])
        else:  # 출발점이 처음 등장한 경우
            Lines[inputLine[i]] = [inputLine[i+1]]

    if caseEnd == 1:  # 케이스 결과 출력 및 입력 초기화
        caseCnt += 1
        nodes = dict()  # 노드 생성
        for key in Lines.keys():
            if key not in nodes:
                nodes[key] = Node(key)
            for value in Lines[key]:
                if value not in nodes:
                    nodes[value] = Node(value)
                nodes[value].canComeFrom.append(key)  # 도착점에 출발점 정보 추가
                nodes[key].canGoTo.append(value)  # 출발점에 도착점 정보 추가

        root = None
        isTree = True
        for nodeItem in nodes.keys():
            if len(nodes[nodeItem].canComeFrom) == 0:  # 들어오는 간선이 없는 노드 찾기
                if root is None:
                    root = nodeItem
                else:  # 루트 노드가 여러 개인 경우
                    isTree = False
                    break

        if root is None:  # 루트 노드가 없는 경우
            isTree = False

        if isTree:
            for nodeItem in nodes.keys():
                if len(nodes[nodeItem].canComeFrom) != 1 and nodeItem != root:  # 루트 노드 외에 들어오는 간선이 여러 개인 노드 찾기
                    isTree = False
                    break
            if len(nodes[root].canComeFrom) > 0:  # 루트 노드에 들어오는 간선이 있는 경우
                isTree = False

        if not any(Lines):  # 입력이 없는 경우
            isTree = True
        if isTree and any(Lines):  # 트리인 경우 레벨 순회 수행
            tree = Tree(nodes[root])
            tree.levelorder(nodes[root])
            for nodeItem in nodes.keys():
                if not nodes[nodeItem].canFromRoot:  # 루트에서 도달할 수 없는 노드 찾기
                    isTree = False
                    break

        if isTree:
            print(f'Case {caseCnt} is a tree.')
        else:
            print(f'Case {caseCnt} is not a tree.')
        Lines = dict()  # 입력 초기화