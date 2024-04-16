T = int(input())  # 테스트 케이스의 수
dp = [0, 1, 1, 1] + [0] * 100  # 초기값 설정 및 dp 리스트 확장

# 동적 프로그래밍으로 파도반 수열 미리 계산
for i in range(4, 101):
    dp[i] = dp[i-2] + dp[i-3]

for _ in range(T):
    N = int(input())
    print(dp[N])
