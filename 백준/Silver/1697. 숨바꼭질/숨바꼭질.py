from queue import Queue

N, K = map(int, input().split())

MAX = 100001
visited = [0 for i in range(MAX)]

def bfs(cur, sec):
    q = Queue()
    q.put((cur, sec))
    visited[cur] = sec
    
    while not q.empty():
        cur, sec = q.get()
        if cur == K:
            break
        
        if cur-1 >= 0 and visited[cur-1] == 0:
            q.put((cur-1, sec+1))
            visited[cur-1]=1
        if cur+1 < MAX and visited[cur+1] == 0:
            q.put((cur+1, sec+1))
            visited[cur+1]=1
        if cur*2 < MAX and visited[cur*2] == 0:
            q.put((cur*2, sec+1))
            visited[cur*2]=1
        
    return sec
        
sec = bfs(N,0)
print(sec)