# 누적합을 이용해 시간복잡도를 최대 O(N*K)으로 줄이기 - 3중 for문은 효율성 통과 X

def solution(board, skill):
    answer = 0
    # 1. 누적합 배열 선언
    matrix = [[0] * (len(board[0]) + 1) for _ in range(len(board) + 1)]  # 누적합 기록을 위한 배열
    
    board_length = len(board)
    board_width = len(board[0])
    matrix_length = len(matrix)

    for type, r1, c1, r2, c2, degree in skill:
        # 2. 누적합 기록
        matrix[r1][c1] += degree if type == 2 else -degree
        matrix[r1][c2 + 1] += -degree if type == 2 else degree
        matrix[r2 + 1][c1] += -degree if type == 2 else degree
        matrix[r2 + 1][c2 + 1] += degree if type == 2 else -degree

    # 3. 행 기준 누적합
    for i in range(matrix_length - 1):
        for j in range(board_width):
            matrix[i][j + 1] += matrix[i][j]

    # 4. 열 기준 누적합
    for j in range(board_width):
        for i in range(matrix_length - 1):
            matrix[i + 1][j] += matrix[i][j]

    # 5. 기존 배열과 합하기
    for i in range(board_length):
        for j in range(board_width):
            board[i][j] += matrix[i][j]
            if board[i][j] > 0:
                answer += 1

    return answer
