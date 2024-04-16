from sys import stdin
input = stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    stickers = [list(map(int, input().split())) for _ in range(2)]
    
    if n == 1:
        print(max(stickers[0][0], stickers[1][0]))
        continue

    # 첫 번째 스티커
    dp = [[0] * n for _ in range(2)]
    dp[0][0] = stickers[0][0]
    dp[1][0] = stickers[1][0]

    # 두 번째 스티커
    for i in range(1, n):
        dp[0][i] = max(dp[1][i-1], dp[1][i-2] if i > 1 else 0) + stickers[0][i]
        dp[1][i] = max(dp[0][i-1], dp[0][i-2] if i > 1 else 0) + stickers[1][i]

    print(max(dp[0][n-1], dp[1][n-1]))