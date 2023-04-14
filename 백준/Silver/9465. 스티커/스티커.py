T = int(input())

for _ in range(T):
    n = int(input())
    stickers = []
    for i in range(2):
        stickers.append(list(map(int, input().split())))
        
    dp = [[0 for _ in range(3)] for _ in range(n)]
    
    for i in range(2):
        dp[0][i] = stickers[i][0]
    dp[0][2] = 0
    
    for j in range(1,n):
        dp[j][0] = max([dp[j-1][1] + stickers[0][j], dp[j-1][2] + stickers[0][j]])
        dp[j][1] = max([dp[j-1][0] + stickers[1][j], dp[j-1][2] + stickers[1][j]])
        dp[j][2] = max([dp[j-1][0], dp[j-1][1]])
        
    print(max(dp[n-1]))