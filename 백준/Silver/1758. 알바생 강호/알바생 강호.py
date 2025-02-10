n = int(input())
line = [int(input()) for i in range(n)]
line = sorted(line)
line.reverse()
tip = 0

for i in range(n):
    if line[i] - i < 0:
        tip += 0
    else:
        tip += line[i] - i
print(tip)