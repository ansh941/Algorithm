from collections import deque

# 가로, 세로
N = int(input())

map_ = []
for i in range(N):
    map_.append(list(map(int, input().split())))

dx = [0,0,-1,1]
dy = [-1,1,0,0]

counts = [0 for _ in range(101)]

for h in range(0, 101):
    visited = [[0 for _ in range(N)] for _ in range(N)]
    
    q = deque()
    count = 0
    locations = []
    for y in range(N):
        for x in range(N):
            if map_[y][x] > h:
                locations.append((x,y))
    if len(locations) == 0:
        break

    for l in locations:
        x,y = l
        if visited[y][x] == 1:
            continue
        q.append((x,y))
        visited[y][x] = 1

        while q:
            x,y = q.popleft()
            
            for i in range(4):
                next_x = x + dx[i]
                next_y = y + dy[i]

                if next_x >= 0 and next_x < N and next_y >= 0 and next_y < N:
                    if map_[next_y][next_x] > h and visited[next_y][next_x] == 0:
                        q.append((next_x, next_y))
                        visited[next_y][next_x] = 1
        count += 1

    counts[h-1] = count

print(max(counts))