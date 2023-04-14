from queue import Queue

dy = [-1, -1, -1, 0, 1, 1, 1, 0]
dx = [-1, 0, 1, 1, 1, 0, -1, -1]

def print_map(m, h):
    for i in range(h):
        print(m[i])
    print()
    
def bfs(y, x):
    q = Queue()
    q.put((y,x))
    visited[y][x] = 1
    while not q.empty():
        y, x = q.get()
        
        for i in range(8):
            next_y = y+dy[i]
            next_x = x+dx[i]
            if next_y >= 0 and next_y < h and next_x >= 0 and next_x < w:
                if m[next_y][next_x] == 1 and visited[next_y][next_x] == 0:
                    q.put((next_y,next_x))
                    visited[next_y][next_x] = 1
        
    
    
while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    m = []
    for i in range(h):
        m.append(list(map(int, input().split())))
        
    visited = [[0 for i in range(w)] for j in range(h)]    
    
    d_cnt = 0
    for i in range(h):
        for j in range(w):
            if visited[i][j] == 0 and m[i][j] == 1:
                bfs(i,j)
                d_cnt += 1
    
    print(d_cnt)