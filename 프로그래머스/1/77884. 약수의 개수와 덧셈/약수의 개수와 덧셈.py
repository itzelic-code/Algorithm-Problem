def solution(left, right):
    answer = 0
    mea = []
    for i in range(left, right + 1):
        for j in range(1, i + 1):
            if i % j == 0:
                mea.append(j)
        if len(mea) % 2 == 0:
            answer += i
        else:
            answer -= i
        mea = []

    return answer