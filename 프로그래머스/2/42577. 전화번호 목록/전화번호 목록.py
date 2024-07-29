def solution(phone_book):
    phone_book.sort()
    
    # 인접한 전화번호끼리 비교
    for i in range(len(phone_book) - 1):
        # 현재 전화번호와 다음 전화번호 비교
        if phone_book[i] == phone_book[i + 1][:len(phone_book[i])]:
            return False  # 접두사 관계가 있음
    
    return True  # 모든 전화번호가 접두사 관계가 없음