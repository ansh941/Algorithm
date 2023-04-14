from collections import deque

N, M = map(int, input().split())

m = []
for i in range(N):
    tmp = input()
    tmp = list(map(int, ' '.join(tmp).split()))
    m.append(tmp)

visited = [[[-1 for _ in range(M)] for _ in range(N)] for _ in range(2)]

cnt = 1
bbu = 0
q = deque()
q.append((0,0, cnt, bbu))
visited[bbu][0][0] = cnt

dy = [-1,1,0,0]
dx = [0,0,-1,1]
while q:
    y, x, cnt, bbu = q.popleft()
    
    for i in range(4):
        next_y = y+dy[i]
        next_x = x+dx[i]
        if next_y >= 0 and next_y < N and next_x >= 0 and next_x < M:
            if bbu==1:
                if m[next_y][next_x] == 0 and visited[bbu][next_y][next_x] == -1:
                    q.append((next_y, next_x, cnt+1, bbu))
                    visited[bbu][next_y][next_x] = cnt+1
            else:
                if visited[bbu][next_y][next_x] == -1:
                    if m[next_y][next_x] == 0:
                        q.append((next_y, next_x, cnt+1, bbu))
                        visited[bbu][next_y][next_x] = cnt+1
                    else:
                        q.append((next_y, next_x, cnt+1, 1))
                        visited[bbu][next_y][next_x] = cnt+1



not_bu = visited[0][N-1][M-1]
bu = visited[1][N-1][M-1]
val = -1
if min([not_bu, bu]) == -1:
    val = max([not_bu, bu])
else:
    val = min([not_bu, bu])
print(val)