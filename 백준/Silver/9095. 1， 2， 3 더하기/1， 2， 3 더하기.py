T = int(input())

for i in range(T):
    n = int(input())
    dp = [0 for _ in range(n+2)]
    dp[0]=1
    dp[1]=2
    dp[2]=4
    for j in range(3, n+2):
        dp[j] = dp[j-1]+dp[j-2]+dp[j-3]
    print(dp[n-1])