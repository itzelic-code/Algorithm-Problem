# 단순 탐색 & 그리디 문제
def solution(m, n, board):
    answer = 0
    board = [list(x) for x in board]
    
    while True:
        target = set()
        
        # 지워지는 블록 좌표 정의
        for i in range(m - 1):
            for j in range(n - 1):
                t = board[i][j]
                # 만약 블록이 비어있거나 같지 않으면 패스
                if t == '' or not (board[i][j] == t and board[i+1][j] == t and board[i][j+1] == t and board[i+1][j+1] == t):
                    continue
                
                # 해당 블록 좌표 추가
                target.add((i, j))
                target.add((i, j+1))
                target.add((i+1, j))
                target.add((i+1, j+1))

        if target:
            # 지워지는 블록 개수 업데이트
            answer += len(target)
            # target 블록 순회하며 지우기
            for i, j in target:
                board[i][j] = ''
        else: # 만약 target 값이 없으면 종료
            break
        
        # 빈 칸 위의 블록 내리기
        for j in range(n):
            # 블록 내리기
            write_index = m - 1  # 아래에서부터 채우기
            for i in range(m - 1, -1, -1):
                if board[i][j] != '':
                    board[write_index][j] = board[i][j]
                    if write_index != i:  # 다른 위치에 값을 쓴 경우
                        board[i][j] = ''  # 원래 위치는 빈 공간으로
                    write_index -= 1

    return answer
