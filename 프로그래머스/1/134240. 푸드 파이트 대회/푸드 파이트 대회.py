def solution(food):
    left = ''
    for i in range(1, len(food)):
        print("i : ", i)
        left += str(i) * (food[i]//2)
        print("left : ", str(left))

    return left + '0' + left[::-1]