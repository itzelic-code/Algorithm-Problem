from sys import stdin

N = int(stdin.readline())
circles = []

for i in range(N):
    x, r = map(int, stdin.readline().split())
    circles.append((x - r, i)) # 원의 왼쪽 끝점
    circles.append((x + r, i)) # 원의 오른쪽 끝점
circles.sort() # 왼쪽부터 차례로 나열

# 왼쪽부터 차례로 stack에 push
stack = []
for c in circles:
    if stack:
        if stack[-1][1] == c[1]:
            stack.pop()
        else:
            stack.append(c)
    else:
        stack.append(c)

if stack:
    print("NO")
else:
    print("YES")