def solution(board, moves):
    stack = []
    answer = 0

    for move in moves:
        for i in range(len(board)):
            if board[i][move-1] != 0:
                picked = board[i][move-1]
                board[i][move-1] = 0

                if stack and stack[-1] == picked:
                    stack.pop()
                    answer += 2
                else:
                    stack.append(picked)
                break

    return answer
