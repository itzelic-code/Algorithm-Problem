from itertools import permutations


def check(users, banned_id):  # 제재 ID와 일치여부 반환 함수
    for user, ban in zip(users, banned_id):  # 사용자 아이디 - 제재 아이디 비교
        if len(user) != len(ban):
            return False
        for u, b in zip(user, ban):  # 아이디 비교
            if b != "*" and b != u:
                return False
    return True

def solution(user_id, banned_id):
    banned_set = set()
    # 사용자 ID 순열 생성 - 제재 아이디 갯수 만큼
    for users in permutations(user_id, len(banned_id)):
        if check(users, banned_id):  # 제대 아이디와 일치 여부
            banned_set.add(tuple(sorted(users)))

    return len(banned_set)