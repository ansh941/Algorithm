n = int(input())

'''
dp[n] = dp[n-1] + dp[n-2]
'''

dp = [0 for _ in range(n+1)]
dp[0] = 1
dp[1] = 1
for i in range(2, n+1):
    dp[i] = dp[i-1]+dp[i-2]
    dp[i] %= 10007
print(dp[n])