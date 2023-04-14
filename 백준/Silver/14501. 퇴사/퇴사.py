from collections import deque

N = int(input())

T = []
P = []
for i in range(N):
    tp = list(map(int, input().split()))
    T.append(tp[0])
    P.append(tp[1])
    
# N : 퇴사까지 남은 날
# N+1 일째 퇴사

# T_i : 상담 완료까지 걸리는 시간
# P_i : 상담할 때 받을 수 있는 금액

# 1일에 잡혀있는 상담은 3일 걸리고 받는 금액은 10.
# 만약 1일에 잡혀있는 상담을 하면 2, 3일의 상담은 못 함
# N+1 일째에는 회사에 없으니 i+T_i가 N+1보다 크면 상담 불가

q = deque()

max_idx = 0
for i in range(N):
    if i+T[i] <= N:
        idx = i
        val = P[i]
        q.append((idx, val))

values = [0 for _ in range(N)]
while q:
    idx, val = q.popleft()
    
    if values[idx] < val:   
        values[idx] = val
        
    st = idx+T[idx]
    for next_idx in range(st, N):
        if next_idx + T[next_idx] <= N:
            q.append((next_idx, val+P[next_idx]))

print(max(values))