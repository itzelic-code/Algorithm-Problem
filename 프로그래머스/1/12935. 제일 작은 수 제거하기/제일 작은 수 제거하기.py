def solution(arr):
    if len(arr) == 1:
        return [-1]
    
    min_value = min(arr)
    new_arr = [num for num in arr if num != min_value]
    
    return new_arr