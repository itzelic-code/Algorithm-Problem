from sys import stdin
input = stdin.readline

def is_valid(n, x, y):
    return not (row_check[x][n] or col_check[y][n] or square_check[x//3][y//3][n])

def toggle(n, x, y, val):
    row_check[x][n] = col_check[y][n] = square_check[x//3][y//3][n] = val

def sudoku(pos):
    if pos == len(blanks):  # 모든 빈 칸을 채움
        for row in board:
            print(''.join(map(str, row)))
        return True
    
    x, y = blanks[pos]
    for n in range(1, 10):
        if is_valid(n, x, y):
            board[x][y] = n
            toggle(n, x, y, True)
            if sudoku(pos + 1):
                return True
            board[x][y] = 0
            toggle(n, x, y, False)
    return False

board = [list(map(int, input().rstrip())) for _ in range(9)]
row_check = [[False] * 10 for _ in range(9)]
col_check = [[False] * 10 for _ in range(9)]
square_check = [[[False] * 10 for _ in range(3)] for _ in range(3)]

blanks = [(x, y) for x in range(9) for y in range(9) if board[x][y] == 0]

for x in range(9):
    for y in range(9):
        n = board[x][y]
        if n:
            toggle(n, x, y, True)

sudoku(0)
