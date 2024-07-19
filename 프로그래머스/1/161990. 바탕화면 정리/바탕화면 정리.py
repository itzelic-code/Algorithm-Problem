def solution(wallpaper):
    # 최소 최대 좌표를 초기화
    min_x, min_y, max_x, max_y = float('inf'), float('inf'), 0, 0

    # 바탕화면을 순회
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
		        # # 발견하면
            if wallpaper[i][j] == '#':
                # 최소 좌표 갱신
                min_x = min(min_x, i)
                min_y = min(min_y, j)
                # 최대 좌표 갱신
                max_x = max(max_x, i + 1)
                max_y = max(max_y, j + 1)

    # 최소 최대 좌표 반환
    return [min_x, min_y, max_x, max_y]
