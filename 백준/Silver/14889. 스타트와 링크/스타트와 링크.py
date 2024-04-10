from itertools import combinations

n = int(input())
scoreboard = [list(map(int, input().split())) for _ in range(n)]
team_with_0s = list(combinations(range(1, n), n // 2 - 1)) # 0번 사람 + (n // 2 - 1)명
m = float('inf') # 출력할 최솟값의 초기값

for team1 in team_with_0s:
  team1 = [0] + list(team1)
  team2 = list(set(range(n)) - set(team1))
  score1 = 0
  score2 = 0
  
  for i in range(n // 2):
    for j in range(n // 2):
      score1 += scoreboard[team1[i]][team1[j]]
      score2 += scoreboard[team2[i]][team2[j]]
  m = min(m, abs(score1 - score2)) # 두 팀 능력치의 차

print(m)