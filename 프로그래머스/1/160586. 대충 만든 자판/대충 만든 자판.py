def solution(keymap, strings):
    answer = []
    
    for string in strings:
        min_press = 0
        for char in string:
            min_press_char = float('inf')
            for key in keymap:
                if char in key:
                    min_press_char = min(min_press_char, key.index(char) + 1)
            if min_press_char == float('inf'):
                min_press = -1
                break
            min_press += min_press_char
        answer.append(min_press)
    
    return answer