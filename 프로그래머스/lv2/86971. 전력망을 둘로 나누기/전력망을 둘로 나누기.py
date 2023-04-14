from collections import deque

def solution(n, wires):
    answer = [0 for _ in range(len(wires))]
    
    wires = list(sorted(wires))
    
    for i in range(len(wires)):
        new_wires = wires.copy()
        
        del new_wires[i]
        
        visited = [0 for _ in range(n)]
        q = deque()
        q.append(1) # 현재 위치
        visited[0] = 1
        
        while q:
            cur = q.popleft()
            
            for w in new_wires:
                if min(w) <= cur:
                    if cur in w:
                        idx = w.index(cur)
                        idx = abs(idx-1) # 0 -> 1 1 -> 0
                        if visited[w[idx]-1] == 0:
                            q.append(w[idx])
                            visited[w[idx]-1] = 1
                else:
                    break
        # print(visited)
        answer[i] = abs(n - sum(visited)*2)
        # print(answer)
    answer = min(answer)        
        
    return answer