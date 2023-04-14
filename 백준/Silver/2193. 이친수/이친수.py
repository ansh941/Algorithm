N = int(input())

dp = [[0 for _ in range(2)] for _ in range(N)]

dp[0][1] = 1
for i in range(1, N):
    for j in range(2):
        if j == 1:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = dp[i-1][j] + dp[i-1][j+1]
print(sum(dp[N-1]))