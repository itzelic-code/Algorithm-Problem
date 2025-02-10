N = int(input())
C = [int(input()) for i in range(N)]
C.sort(reverse=True)

answer = 0
for i in range(2, len(C), 3):
  answer += C[i]

print(sum(C) - answer)