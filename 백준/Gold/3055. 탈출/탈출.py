from collections import deque

R, C = map(int, input().split())

m = []
for i in range(R):
    tmp = input()
    tmp = ' '.join(tmp).split()
    m.append(tmp)
    
y, x, wy, wx, dy, dx = 0,0,[],[],0,0
for i in range(R):
    for j in range(C):
        if m[i][j] == '*':
            wy.append(i)
            wx.append(j)
            
        if m[i][j] == 'S':
            y = i
            x = j
            
        if m[i][j] == 'D':
            dy = i
            dx = j
            
visited = [[0 for _ in range(C)] for _ in range(R)]
w_visited = [[float('inf') for _ in range(C)] for _ in range(R)]

diry = [-1, 1, 0, 0]
dirx = [0 ,0, -1, 1]

cnt = 1
w_q = deque() # 물 큐
for i in range(len(wy)):
    w_y, w_x = wy[i], wx[i]
    w_q.append((w_y, w_x, cnt))
    w_visited[w_y][w_x] = 1
    
    while w_q:
        w_y, w_x, cnt = w_q.popleft()
        
        for i in range(4):                
            next_wy = w_y+diry[i]
            next_wx = w_x+dirx[i]
            if next_wy >= 0 and next_wy < R and next_wx >= 0 and next_wx < C:
                if m[next_wy][next_wx] == '.' or m[next_wy][next_wx] == 'S':
                    if cnt+1 < w_visited[next_wy][next_wx]:
                        w_q.append((next_wy,next_wx, cnt+1))
                        w_visited[next_wy][next_wx] = cnt+1
                        
cnt=1
g_q = deque() # 고슴도치 큐
g_q.append((y, x, cnt))
visited[y][x] = 1

while g_q:
    y, x, cnt = g_q.popleft()
    
    if y == dy and x == dx:
        break
    for i in range(4):
        next_y = y+diry[i]
        next_x = x+dirx[i]
        if next_y >= 0 and next_y < R and next_x >= 0 and next_x < C:
            if m[next_y][next_x] == '.' or m[next_y][next_x] == 'D':
                if visited[next_y][next_x] == 0 and cnt+1 < w_visited[next_y][next_x]:
                    g_q.append((next_y,next_x,cnt+1))
                    visited[next_y][next_x] = cnt+1
# for i in range(R):
#     print(w_visited[i])
# print()
# for i in range(R):
#     print(visited[i])
if visited[dy][dx] == 0:
    print('KAKTUS')
else:
    print(visited[dy][dx]-1)