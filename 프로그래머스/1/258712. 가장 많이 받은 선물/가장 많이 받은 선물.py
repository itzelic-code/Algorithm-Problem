# 주고 받은 선물 정보 표
def make_gifts_table(friends, gifts):
    num_friends = len(friends)
    # 선물 지수 값을 위한 공간 포함하여 테이블 초기화
    table_gifts = [[0 for _ in range(num_friends + 1)] for _ in range(num_friends)]
    for gift in gifts:
        sender, receiver = gift.split()
        table_gifts[friends.index(sender)][friends.index(receiver)] += 1
    
    # 선물 지수 계산
    for i, data in enumerate(table_gifts):    
        table_gifts[i][num_friends] = sum(data) - sum([row[i] for row in table_gifts])
    return table_gifts

def solution(friends, gifts):
    answer = 0
    num_friends = len(friends)
    table_gifts = make_gifts_table(friends, gifts)
    
    # 다음 달에 받을 선물의 수
    list_gifts = [0 for _ in range(num_friends)]    
    for i in range(num_friends):
        # 순회 범위 조정
        for j in range(i + 1, num_friends):
            # 선물을 주고받은 기록이 있는 경우
            if (table_gifts[i][j] != 0 or table_gifts[j][i] != 0) and (table_gifts[i][j] != table_gifts[j][i]):
                list_gifts[i if table_gifts[i][j] > table_gifts[j][i] else j] += 1
            else:
                # 선물 지수 값 비교
                if table_gifts[i][num_friends] > table_gifts[j][num_friends]:
                    list_gifts[i] += 1
                elif table_gifts[i][num_friends] < table_gifts[j][num_friends]:
                    list_gifts[j] += 1
    return max(list_gifts)