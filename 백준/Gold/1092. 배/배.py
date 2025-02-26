import sys
input = sys.stdin.readline

N = int(input())
crane = sorted(list(map(int, input().split())), reverse=True)
M = int(input())
box = sorted(list(map(int, input().split())), reverse=True)
cnt = 0

if box[0] > crane[0]:
    print(-1)
else:
    while box:
        for c in crane:
            if box and c < box[-1]:
                continue
            for b in box:
                if c >= b:
                    box.remove(b)
                    break
        cnt += 1
    print(cnt)
