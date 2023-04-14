from collections import deque

N, K = map(int, input().split())

MAX = 100001
visited = [0 for i in range(MAX)]
secs = [0 for i in range(MAX)]

def bfs(cur,sec):
    q = deque()
    q.append((cur, sec))
    visited[cur] = 1
    
    while q:
        cur, sec = q.popleft()
        if cur == K:
            break
        
        if cur*2 < MAX and visited[cur*2] == 0:
            q.appendleft((cur*2, sec))
            visited[cur*2]=1
            secs[cur*2] = sec
        if cur-1 >= 0 and visited[cur-1] == 0:
            q.append((cur-1, sec+1))
            visited[cur-1]=1
            secs[cur-1] = sec+1
        if cur+1 < MAX and visited[cur+1] == 0:
            q.append((cur+1, sec+1))
            visited[cur+1]=1
            secs[cur+1] = sec+1
        
    return secs[cur]
        
sec = bfs(N,0)
print(sec)