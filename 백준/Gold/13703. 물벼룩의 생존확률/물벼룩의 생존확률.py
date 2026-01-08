k, n = map(int, input().split())

dp = [[0] * (k + n + 2) for _ in range(n + 1)]
if k == 0:
    print(0)
else:
    dp = [[0] * (k + n + 2) for _ in range(n + 1)]
    dp[0][k] = 1
    for i in range(1, n + 1):
        for j in range(1, k + n + 1):
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]
        dp[i][0] = 0 

    print(sum(dp[n]))