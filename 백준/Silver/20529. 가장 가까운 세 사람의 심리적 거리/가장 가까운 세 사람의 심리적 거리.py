from itertools import combinations

T = int(input())

for _ in range(T):
    N = int(input())
    mbtis = input().split()
    if N > 32:  # 같은 MBTI가 최소 3개 존재
        print(0)
    else:
        min_distance = float('inf')
        for comb in combinations(mbtis, 3):
            distance = sum(a != b for a, b in zip(comb[0], comb[1])) + sum(a != b for a, b in zip(comb[0], comb[2])) + sum(a != b for a, b in zip(comb[1], comb[2]))
            min_distance = min(min_distance, distance)
        print(min_distance)
