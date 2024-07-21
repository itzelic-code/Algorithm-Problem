def distance(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

def solution(numbers, hand):
    answer = ''
    
    # 왼손과 오른손의 현재 위치
    left_pos = '*'
    right_pos = '#'
    
    # 각 숫자의 위치를 나타내는 딕셔너리
    num_pos = {
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), 9: (2, 2),
        '*': (3, 0), 0: (3, 1), '#': (3, 2)
    }
    
    for num in numbers:
        # 1, 4, 7은 왼손
        if num in [1, 4, 7]:
            answer += 'L'
            left_pos = num
        # 3, 6, 9는 오른손
        elif num in [3, 6, 9]:
            answer += 'R'
            right_pos = num
        # 2, 5, 8, 0은 가까운 손
        else:
            left_dist = distance(num_pos[num], num_pos[left_pos])
            right_dist = distance(num_pos[num], num_pos[right_pos])
            
            if left_dist < right_dist:
                answer += 'L'
                left_pos = num
            elif left_dist > right_dist:
                answer += 'R'
                right_pos = num
            else:
                if hand == 'left':
                    answer += 'L'
                    left_pos = num
                else:
                    answer += 'R'
                    right_pos = num
    
    return answer
