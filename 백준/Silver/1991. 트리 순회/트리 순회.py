class TreeNode:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None

def preorder(node):
    if node is None:
        return
    print(node.name, end='')  # 루트 처리
    preorder(node.left)  # 왼쪽 서브트리 순회
    preorder(node.right)  # 오른쪽 서브트리 순회

def inorder(node):
    if node is None:
        return
    inorder(node.left)  # 왼쪽 서브트리 순회
    print(node.name, end='')  # 루트 처리
    inorder(node.right)  # 오른쪽 서브트리 순회

def postorder(node):
    if node is None:
        return
    postorder(node.left)  # 왼쪽 서브트리 순회
    postorder(node.right)  # 오른쪽 서브트리 순회
    print(node.name, end='')  # 루트 처리

N = int(input())
tree = {}

for _ in range(N):
    root, left, right = input().split()
    if root not in tree:
        tree[root] = TreeNode(root)
    if left != '.':
        tree[root].left = TreeNode(left)
        tree[left] = tree[root].left
    if right != '.':
        tree[root].right = TreeNode(right)
        tree[right] = tree[root].right

preorder(tree['A'])
print()
inorder(tree['A'])
print()
postorder(tree['A'])
