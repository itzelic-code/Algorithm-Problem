def solution(want, number, discount):
    # 상품 - 수량 dict
    want_dict = {want[i]: number[i] for i in range(len(want))}
    count = 0
    discount_length = len(discount)

    # 슬라이딩 윈도우
    for i in range(discount_length - 9):  # 10일 동안 할인 행사
        current_discount = discount[i:i + 10]  # 10일 동안 할인 상품
        current_count = {}

        # 할인 상품 수량 계산
        for item in current_discount:
            if item in want_dict:
                current_count[item] = current_count.get(item, 0) + 1

        # 수량 확인
        if all(current_count.get(item, 0) >= want_dict[item] for item in want_dict):
            count += 1

    return count