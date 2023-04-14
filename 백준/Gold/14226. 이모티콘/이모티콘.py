from queue import Queue

S = int(input())

MAX = 1001
visited = [[0 for i in range(MAX)] for j in range(MAX)]

def bfs(s, c):
    count = 0
    q = Queue()
    q.put((s,c,count))
    visited[s][c]=1
    while not q.empty():
        s,c,count = q.get()
        if s == S:
            break
        
        if s != c:
            q.put((s,s, count+1))
            visited[s][s]=1
            
        if s+c < MAX and visited[s+c][c] == 0:
            q.put((s+c,c,count+1))
            visited[s+c][c] = 1
            
        if s-1 >= 0 and visited[s-1][c] == 0:
            q.put((s-1,c,count+1))
            visited[s-1][c]=1
            
    return count

cnt = bfs(1,0)
print(cnt)
