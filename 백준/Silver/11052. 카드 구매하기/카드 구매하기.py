n = int(input())

p = list(map(int, input().split()))
dp = [0 for i in range(n+1)]

dp[0] = 0
dp[1] = p[0]
for i in range(1, n+1):
    val = 0
    for j in range(i):
        if val < p[j] + dp[i-j-1]:
            val = p[j] + dp[i-j-1]
            
    dp[i] = val
print(dp[n])