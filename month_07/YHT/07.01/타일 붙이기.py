T = int(input())
cases = [int(input()) for _ in range(T)]

dp = [0] * 31
dp[0] = 1
dp[1] = 1
dp[2] = 3  

for i in range(3, 31):
    dp[i] = dp[i-1] + 2 * dp[i-2] + dp[i-3]

for i, n in enumerate(cases, 1):
    print(f"#{i} {dp[n]}")