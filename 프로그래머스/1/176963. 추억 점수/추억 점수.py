def solution(name, yearning, photo):
    answer = []
    for row in photo:
        cnt = 0
        for n in name:
            if n in row:
                cnt += yearning[name.index(n)]
        answer.append(cnt)
    return answer