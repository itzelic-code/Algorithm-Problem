def solution(s):
    answer = []
    s = s[2:-2].split("},{")
    s.sort(key=len)

    for i in s:
        for j in i.split(","):
            if j not in answer:
                answer.append(j)
    return list(map(int, answer))