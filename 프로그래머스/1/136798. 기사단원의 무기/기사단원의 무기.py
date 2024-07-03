def solution(number, limit, power):
    cnt = 0
    for i in range(1, number + 1):
        mea = 0
        for j in range(1, int(i ** 0.5) + 1):
            if i % j == 0:
                mea += 1
                if j != i//j:
                    mea += 1
        if mea > limit:
            mea = power
        cnt += mea
    return cnt