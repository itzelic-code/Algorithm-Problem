from sys import stdin
input = stdin.readline

N = int(input())
K = int(input())
sensors = list(map(int, input().split()))

# 센서가 집중국보다 적거나 같을 때
if K >= N:
    print(0)
else:
    sensors.sort()
    distances = []
    
    for i in range(1, N):
        distances.append(sensors[i] - sensors[i-1])
    
    distances.sort()
    for _ in range(K-1):
        distances.pop()
    
    print(sum(distances))