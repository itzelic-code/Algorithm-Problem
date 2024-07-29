# 깊이 우선 탐색(DFS)를 이용한 풀이
def solution(numbers, target):
    def dfs(index, total):
        # 모든 숫자를 사용한 경우
        if index == len(numbers):
            return 1 if total == target else 0
        
        return (dfs(index + 1, total + numbers[index]) +
                dfs(index + 1, total - numbers[index]))

    return dfs(0, 0)