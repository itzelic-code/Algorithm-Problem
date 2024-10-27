from itertools import combinations


def solution(places):
    answer = []

    def rule(case):
        for c in case:
            x1, y1 = c[0]  # 첫 번째 사람 좌표
            x2, y2 = c[1]  # 두 번째 사람 좌표
            d = abs(x1 - x2) + abs(y1 - y2)  # 맨해튼 거리 계산

            # 맨해튼 거리가 2 이내인 경우
            if (d <= 2):
                # 같은 행에 있을 때
                if (x1 == x2):
                    # 두 사람 사이에 파티션 없는지 확인
                    if (map[x1][max(y1, y2) - 1] != 'X'):
                        return False
                # 같은 열에 있을 때
                elif (y1 == y2):
                    # 두 사람 사이에 파티션 없는지 확인
                    if (map[max(x1, x2) - 1][y1] != 'X'):
                        return False
                # 대각선에 있을 때
                else:
                    # 대각선 위치에 파티션 없는지 확인
                    if (map[x1][y2] != 'X') or (map[x2][y1] != 'X'):
                        return False

        return True  # 모든 케이스 통과 시 True

    for case in places:
        map = []
        for line in case:
            map.append(list(i for i in line))

        location = []
        for row in range(5):
            for col in range(5):
                if (map[row][col] == 'P'):
                    location.append([row, col])  # 사람 위치 저장

        case = list(combinations(location, 2))  # 모든 사람 쌍 조합
        if rule(case):  # 거리두기 규칙 지켰을 경우
            answer.append(1)
        else:  # 거리두기 규칙 위반했을 경우
            answer.append(0)

    return answer