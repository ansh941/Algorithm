from collections import deque

M, N = map(int, input().split())

m = []
for i in range(N):
    tmp = input()
    m.append(list(map(int, ' '.join(tmp).split())))

visited = [[0 for i in range(M)] for j in range(N)]
counts = [[0 for i in range(M)] for j in range(N)]

def bfs(y, x):
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1 ,1]
    
    cnt = 0
    q = deque()
    q.append((y,x,cnt))
    
    while q:
        y, x, cnt = q.popleft()
        
        if y == N-1 and x == M-1:
            break
        
        for i in range(4):
            if y+dy[i] >= 0 and y+dy[i] < N and x+dx[i] >= 0 and x+dx[i] < M:
                next_y = y+dy[i]
                next_x = x+dx[i]
                if visited[next_y][next_x] == 0:
                    
                    if m[next_y][next_x] == 1:
                        q.append((next_y, next_x, cnt+1))
                        visited[next_y][next_x] = 1
                        counts[next_y][next_x] = cnt+1
                    else:
                        q.appendleft((next_y, next_x, cnt))
                        visited[next_y][next_x] = 1
                        counts[next_y][next_x] = cnt
    return counts[y][x]

count = bfs(0,0)
print(count)
