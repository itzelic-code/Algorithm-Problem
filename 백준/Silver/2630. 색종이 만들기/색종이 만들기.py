def solve(x, y, n):
    global white, blue
    color = paper[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if paper[i][j] != color:
                for k in range(2):
                    for l in range(2):
                        solve(x+k*n//2, y+l*n//2, n//2)
                return
    if color == 0:
        white += 1
    else:
        blue += 1

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
white, blue = 0, 0
solve(0, 0, N)
print(white)
print(blue)
