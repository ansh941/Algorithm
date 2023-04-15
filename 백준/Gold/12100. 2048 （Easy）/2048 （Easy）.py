from collections import deque
from copy import deepcopy

def get_sum(b):
    s = 0
    for i in range(N):
        s += sum(b[i])
    return s

def get_max(b):
    m = 0
    for i in range(N):
        m = max(m, max(b[i]))
    return m

def up(b, N):
    for i in range(N - 1):
        for j in range(N):
            k = i+1
            while k < N:
                if b[i][j] == 0:
                    b[i][j] = b[k][j]
                    b[k][j] = 0
                    k += 1
                    continue

                if b[k][j] != 0:
                    # 같으면 합쳐짐
                    if b[i][j] == b[k][j]:
                        b[i][j] *= 2
                        b[k][j] = 0
                    break
                k+=1

    return b


def clock_rotation(b, angle, N):
    # 시계 방향 회전
    for _ in range(angle):
        b = list(map(list, zip(*b[::-1])))

    return b

def counterclock_rotation(b, angle, N):
    # 반시계 방향 회전
    for _ in range(angle):
        b = list(map(list, zip(*b)))[::-1]

    return b

def print_board(b, N):
    for i in range(N):
        print(b[i])
    print()


N = int(input().strip())

board = []
for i in range(N):
    tmp = input().strip()
    tmp = list(map(int, ''.join(tmp).split()))
    board.append(tmp)

s = get_sum(board)
result = get_max(board)

q = deque()
q.append((0, board))

visited = [board]

move = [1, 0, 1, 2, 1]

while q:
    cur_n, cur_b = q.popleft()
    result = max(result, get_max(cur_b))

    if cur_n >= 5:
        continue

    # 상 좌 하 우
    for i in range(4):
        next_b = deepcopy(cur_b)
        next_b = up(clock_rotation(next_b, i,N),N)
        next_b = counterclock_rotation(next_b, i,N)
        if next_b not in visited:
            q.append((cur_n + 1, next_b))
            visited.append(next_b)
            if get_sum(next_b) != s:
                print(cur_n+1, get_sum(next_b))
                print_board(next_b, N)
print(result)