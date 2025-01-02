import sys
input = sys.stdin.readline

class Node:
    def __init__(self, data, left_node, right_node):
        self.data = data
        self.left_node = left_node
        self.right_node = right_node

# 전위 순회 (Pre-order Traversal)
def pre_order(node):
    print(node.data, end='') # 자기 자신을 먼저 출력
    if node.left_node != None:
        pre_order(tree[node.left_node])
    if node.right_node != None:
        pre_order(tree[node.right_node])

# 중위 순회 (In-order Traversal)
def in_order(node):
    if node.left_node != None:
        in_order(tree[node.left_node])
    print(node.data, end='')
    if node.right_node != None:
        in_order(tree[node.right_node])

# 후위 순회 (Post-order Traversal)
def post_order(node):
    if node.left_node != None:
        post_order(tree[node.left_node])
    if node.right_node != None:
        post_order(tree[node.right_node])
    print(node.data, end='')

# 입력
n = int(input().rstrip())
tree = {}

for i in range(n):
    data, left_node, right_node = input().rstrip().split()
    if left_node == ".":
        left_node = None
    if right_node == ".":
        right_node = None
    tree[data] = Node(data, left_node, right_node)

# 순회 함수 호출
pre_order(tree['A'])
print()
in_order(tree['A'])
print()
post_order(tree['A'])