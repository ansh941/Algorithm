N = int(input())

num_edge = int(input())
edges = []
for i in range(num_edge):
    s,t = map(int, input().split())
    edges.append([s,t])

from collections import deque

q = deque()
q.append(1)

visited = [0 for _ in range(N+1)]
visited[1] = 1
        
while q:
    cur = q.popleft()
    
    for i in range(1, N+1):
        if [cur,i] in edges or [i, cur] in edges:
            if visited[i] == 0:
                q.append(i)
                visited[i]=1
print(sum(visited)-1)