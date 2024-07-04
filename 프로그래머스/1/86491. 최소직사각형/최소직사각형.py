def solution(sizes):
    max_w = 0
    max_h = 0

    for w, h in sizes:
            # 최대 가로
            max_w = max(max_w, max(w, h))
            # 최대 세로
            max_h = max(max_h, min(w, h))

    return max_w * max_h