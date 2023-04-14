from collections import deque

N, M = map(int, input().split())

r, c, d = map(int, input().split())

m = []
for i in range(N):
    m.append(list(map(int, input().split())))
    
#     북  동 남 서
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

# 왼쪽 회전 : 0->3 1->0 2->1 3->2
next_dir = [3, 0, 1, 2]

# 후진
back = [2, 3, 0, 1]

q = deque()
q.append((r, c, d))

visited = [[0 for i in range(M)] for i in range(N)]
visited[r][c] = 1

while q:
    y, x, d = q.popleft()
    
    for i in range(5):
        if i == 4:
            break
        search_d = next_dir[d]
        search_y = y+dy[search_d]
        search_x = x+dx[search_d]
        
        if m[search_y][search_x] == 0 and visited[search_y][search_x] == 0:
            q.append((search_y, search_x, search_d))
            visited[search_y][search_x] = 1
            break
        d = search_d
    
    if i == 4:
        next_y = y+dy[back[d]]
        next_x = x+dx[back[d]]
        if m[next_y][next_x] == 0:
            q.append((next_y, next_x, d))
        else:
            break
        

result = []
for i in range(N):
    result.append(sum(visited[i]))
print(sum(result))