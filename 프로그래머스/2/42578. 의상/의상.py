from collections import defaultdict

def solution(clothes):
    # 의상 종류별로 의상을 분류
    clothes_dict = defaultdict(int)
    
    for name, kind in clothes:
        clothes_dict[kind] += 1

    # 조합 계산
    answer = 1
    for count in clothes_dict.values():
        answer *= (count + 1)

    return answer - 1  # 아무것도 안입는 경우 빼기