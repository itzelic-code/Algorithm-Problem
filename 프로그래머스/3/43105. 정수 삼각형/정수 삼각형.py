def solution(triangle):
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            if j == 0:  # 왼쪽 끝
                triangle[i][j] += triangle[i - 1][0]
            elif j == len(triangle[i]) - 1:  # 오른쪽 끝
                triangle[i][j] += triangle[i - 1][-1]
            else:  # 가운뎃 값
                triangle[i][j] += max(triangle[i - 1][j], triangle[i - 1][j - 1])

    return max(triangle[-1])