from collections import deque
from copy import deepcopy

from itertools import combinations

import time
def get_zero_num(cur_m):
    num = 0
    for i in range(N):
        num += cur_m[i].count(0)
    return num

def spread_virus(N,M,m, cur_add_walls, q, visited, cur_maximum):
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    
    cur_m = deepcopy(m)
    for coord in cur_add_walls:
        y,x = list(coord)[0]
        cur_m[y][x] = 1
    
    cur_safe_count = get_zero_num(cur_m)
    while q:
        if cur_safe_count < cur_maximum:
            return cur_maximum
        cur_y, cur_x = q.popleft()

        for i in range(4):
            next_y = cur_y + dy[i]
            next_x = cur_x + dx[i]
            
            if (next_y, next_x) in visited:
                continue

            if next_y >= 0 and next_y < N and next_x >= 0 and next_x < M:
                if cur_m[next_y][next_x] == 0:
                    q.append((next_y, next_x))
                    cur_m[next_y][next_x] = 2
                    cur_safe_count-=1
    return cur_safe_count

N, M = map(int, input().split())

m = []
for _ in range(N):
    m.append(list(map(int, input().split())))

q = deque()
visited = []

wall_candidates = []
virus = deque()
v_visited = []
for i in range(N):
    for j in range(M):
        if m[i][j] == 0:
            q.append({(i,j)})
            visited.append({i,j})
            wall_candidates.append((i,j))
        elif m[i][j] == 2:
            virus.append((i,j))
            v_visited.append((i,j))


result = 0

def print_map(cur_m):
    for i in range(N):
        print(cur_m[i])

for comb in combinations(q, 3):
    cur_add_walls = comb
    result = spread_virus(N, M, m, cur_add_walls, deepcopy(virus), deepcopy(v_visited), result)
print(result)