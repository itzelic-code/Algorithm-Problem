def solution(board, h, w):
    cnt, n = 0, len(board)
    dh, dw = [0, 1, -1, 0], [1, 0, 0, -1]
    for i in range(4):
        h_check = h + dh[i]
        w_check = w + dw[i]
        if 0 <= h_check < n and 0 <= w_check < n and board[h][w] == board[h_check][
            w_check]:
            cnt += 1
    return cnt