def solution(citations):
    h_index = 0
    citations.sort(reverse=True)
    
    for i in range(len(citations)):
        if citations[i] >= i + 1:
            h_index = i + 1
        else:
            break
    return h_index