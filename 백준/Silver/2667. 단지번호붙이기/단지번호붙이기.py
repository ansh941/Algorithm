N = int(input())

m = []
for i in range(N):
    s = input()
    s = list(map(int,' '.join(s).split()))
    m.append(s)
    
    
visited = [[0 for i in range(N)] for j in range(N)] # 방문 기입
d = [[0 for i in range(N)] for j in range(N)] # 단지 기입


#    상 하 좌 우
dy = [1,-1,0,0]
dx = [0,0,-1,1]
def dfs(x, y):
    global count
    if visited[y][x] == 1 or m[y][x] == 0:
        return
    
    visited[y][x] = 1
    d[y][x] = count
    count+=1
    for i in range(4):
        next_x = x + dx[i]
        next_y = y + dy[i]
        if next_x >= 0 and next_x < N and next_y >= 0 and next_y < N:
            dfs(next_x, next_y)
    
        
d_cnt = 0
c_list = []
count = 0
for i in range(N):
    for j in range(N):
        count = 0
        if (visited[i][j] == 0) and (m[i][j] == 1):
            dfs(j, i)
            d_cnt+=1
            c_list.append(count)
            
            
print(d_cnt)
c_list.sort()
if len(c_list) == 0:
    print(count)
else:
    for i in range(d_cnt):
        print(c_list[i])
