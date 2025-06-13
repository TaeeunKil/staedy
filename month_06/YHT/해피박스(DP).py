"""
dp
"""
def dfs():
    pass
T = int(input())
for i in range(1, T + 1):
    N, M = map(int, input().split())
    q = []
    for x in range(M):
        Si, Pi = map(int, input().split())
        q.append((Si, Pi))
    # dp[w] = 무게 w일 때 얻을 수 있는 최대 가치
    dp = [0] * (N + 1)

    for si, pi in q:
        # 거꾸로 가야 중복 선택을 방지할 수 있음
        for w in range(N, si - 1, -1):
            dp[w] = max(dp[w], dp[w - si] + pi)

    print(f"#{i} {max(dp)}") 