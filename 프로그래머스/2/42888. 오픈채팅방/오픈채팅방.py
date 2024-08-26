def solution(record):
    answer = []
    user = {}
    
    # 사용자 정보 저장
    for r in record:
        v = r.split()
        
        # Enter이나 Change일 경우 사용자 이름 업데이트
        if v[0] in ['Enter', 'Change']:
            user[v[1]] = v[2]
    
    # 메시지 생성
    for r in record:
        v = r.split()
        if v[0] == 'Enter':
            # 들어온 메시지
            answer.append(f'{user[v[1]]}님이 들어왔습니다.')
        elif v[0] == 'Leave':
            # 나간 메시지
            answer.append(f'{user[v[1]]}님이 나갔습니다.')
    
    return answer