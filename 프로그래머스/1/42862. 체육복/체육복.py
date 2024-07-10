def solution(n, lost, reserve):
    # 체육복을 도난당한 학생과 여분의 체육복을 가진 학생의 중복을 제거
    # 잃어버린 학생과 여벌 가져온 학생의 중복 제거
    new_lost = set(lost) - set(reserve)
    new_reserve = set(reserve) - set(lost)
    
    for student in new_reserve:
        # 여분의 체육복을 가진 학생이 빌려줌
        if student - 1 in new_lost:
            new_lost.remove(student - 1)
        elif student + 1 in new_lost:
            new_lost.remove(student + 1)
    
    return n - len(new_lost)