import sys
input = sys.stdin.readline

A, B = input().split()
x, a, b = 0, 0, 0
count = 0


for i in range(2, 37):
    try:
        a_temp = int(A, i)
    except:
        continue
    for j in range(2, 37):
        try:
            b_temp = int(B, j)
            if a_temp == b_temp:
                count += 1
                x = a_temp
                a = i
                b = j
        except:
            continue

if count == 1:
    print(x,a,b)
elif count == 0:
    print("Impossible")
else:
    print("Multiple")