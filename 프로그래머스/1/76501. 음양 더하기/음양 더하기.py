def solution(absolutes, signs):
    for i in range (len(absolutes)):
        if not signs[i]:
            absolutes[i] = -absolutes[i]
    return sum(absolutes)