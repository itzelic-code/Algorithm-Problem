def solution(board):
    rows = len(board)
    cols = len(board[0])
    max_length = 0  # 한 변의 최대 길이

    dp = [[0] * cols for _ in range(rows)]  # 변의 길이를 저장하는 dp 배열

    for i in range(rows):
        for j in range(cols):
            if board[i][j] == 1:
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1],
                                   dp[i - 1][j - 1]) + 1
                max_length = max(max_length, dp[i][j])
    return max_length**2