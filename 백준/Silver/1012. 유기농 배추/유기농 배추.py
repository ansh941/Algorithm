from collections import deque

# 테스트 케이스 수
T = int(input())

# 상 하 좌 우
dx = [0,0,-1,1]
dy = [-1,1,0,0]

for t in range(T):
    # 가로, 세로, 배추 수
    M,N,K = map(int, input().split())

    # 맵
    map_ = [[0 for _ in range(M)] for _ in range(N)]
    
    # 영역 수
    count = 0
    
    # 배추 위치
    locations = []
    for _ in range(K):
        x,y = map(int, input().split())
        map_[y][x] = 1
        locations.append((x,y))
        
    visited = [[0 for _ in range(M)] for _ in range(N)]
    for l in locations:
        q = deque()
        x,y = l
        q.append((x,y))
        if visited[y][x] == 1:
            continue
        visited[y][x] = 1
    
        while q:
            x,y = q.popleft()
            
            for i in range(4):
                next_x = x + dx[i]
                next_y = y + dy[i]
                
                if next_x >= 0 and next_x < M and next_y >= 0 and next_y < N:
                    if map_[next_y][next_x] == 1 and visited[next_y][next_x] == 0:
                        visited[next_y][next_x] = 1
                        q.append((next_x, next_y))
        count += 1
    print(count)