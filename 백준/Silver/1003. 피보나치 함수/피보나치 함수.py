def fibonacci(n):
    zero = [1, 0]
    one = [0, 1]
    if n <= 1:
        return
    for i in range(2, n+1):
        zero.append(zero[i-1] + zero[i-2])
        one.append(one[i-1] + one[i-2])
    return zero, one

zero, one = fibonacci(40)
for _ in range(int(input())):
    n = int(input())
    print(zero[n], one[n])
