from collections import deque

M,N = map(int, input().split())


map_ = []
count = 0

locations = []
for y in range(N):
    hor = list(map(int, input().split()))
    count += hor.count(0)
    map_.append(hor)
    for x in range(M):
        if hor[x] == 1:
            locations.append([x,y])

dy = [-1,1,0,0]
dx = [0,0,-1,1]

days = 0
visited = [[0 for _ in range(M)] for _ in range(N)]
while count > 0:
    if len(locations) == 0:
        break
    next_locations = []
    for x,y in locations:
        q = deque()
        q.append((x,y))
        visited[y][x] = 1
        
        while q:
            x,y = q.popleft()

            for i in range(4):
                next_x = x + dx[i]
                next_y = y + dy[i]
            
                if next_x >= 0 and next_x < M and next_y >=0 and next_y < N:
                    if map_[next_y][next_x] == 0 and visited[next_y][next_x] == 0:
                        map_[next_y][next_x] = 1
                        next_locations.append((next_x, next_y))
                        visited[next_y][next_x] = 1
                        count -= 1
    days += 1
    locations = next_locations

if count == 0:
    print(days)
else:
    print(-1)