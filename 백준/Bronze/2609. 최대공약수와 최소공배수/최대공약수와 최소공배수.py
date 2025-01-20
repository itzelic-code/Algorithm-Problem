# 입력
a, b = map(int, input().split())

# 최대공약수(GCD) 구하기
def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

# 최소공배수(LCM) 구하기
def lcm(x, y):
    return x * y // gcd(x, y)

print(gcd(a, b))
print(lcm(a, b))
