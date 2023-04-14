from collections import deque
# N : 보드의 크기
# K : 사과의 개수
N = int(input())
K = int(input())

# Rs : 사과의 위치 중 행
# Cs : 사과의 위치 중 열
Rs, Cs = [], []
for _ in range(K):
    tmp = list(map(int, input().split()))
    Rs.append(tmp[0])
    Cs.append(tmp[1])

# L : 방향 변환 횟수
# X : 방향 전환 시간
# C : 방향
L = int(input())
X, C = [], []
for _ in range(L):
    tmp = input().split()
    X.append(int(tmp[0]))
    C.append(tmp[1])


# 맵 생성
m = []
for i in range(N):
    c = []
    for j in range(N):
        char = '.'
        for k in range(K):
            if i == Rs[k]-1 and j == Cs[k]-1:
                char = 'A'
                break
            else:
                char = '.'
        c.append(char)
    m.append(c)
    
m[0][0] = 'S'
# snake : 뱀 몸통 위치
snake = deque()
snake.append((0,0, 3))

count = 0
length = 1
# 뱀의 진행 방향 : 상 하 좌 우
# u : (L, l), (D, r)
# d : (L, r), (D, l)
# l : (L, d), (D, u)
# r : (L, u), (D, d)
# direction = ['u', 'd', 'l', 'r']
next_dir = [[2,3],
            [3,2],
            [1,0],
            [0,1]]
dy = [-1, 1, 0, 0]
dx = [0 ,0, -1, 1]

while True:
    # 현재 위치 및 방향
    y, x, d = snake.popleft()
    
    # 다음 위치
    next_y = 0
    next_x = 0
    for i in range(4):
        if i == d:
            next_y = y+dy[i]
            next_x = x+dx[i]
            
    # 다음 방향
    # 어느 시점에 방향을 전환할 수 있다.
    next_d = d
    for i in range(L):
        if count+1 == X[i]:
            if C[i] == 'L':
                next_d = next_dir[d][0]
            else:
                next_d = next_dir[d][1]
                
    # 다음 위치와 방향이 정해졌다면 count+=1
    count+=1
    
    # 게임이 끝나는지 알려주는 flag
    # 끝 : True
    # 끝x : False
    flag = False
    
    # 벽인지 확인
    if next_y >= 0 and next_y < N and next_x >= 0 and next_x < N:
        # points : 현재 머리를 제외한 나머지 좌표들
        points=[]
        for i in range(1,length):
            s_y,s_x,s_d = snake.popleft()
            points.append((s_y, s_x))
            snake.append((s_y, s_x, s_d))
        # 사과일 경우
        # 길이 + 1
        if m[next_y][next_x] == 'A':
            length+=1
            snake.appendleft((y,x,d))
            snake.appendleft((next_y,next_x,next_d))
            m[next_y][next_x] = 'S'
        else:
            # 일반 이동
            snake.append((next_y, next_x, next_d))
            m[next_y][next_x] = 'S'
            for i in range(1,length):
                m[y][x] = '.'
                ny, nx, nd = y, x, d
                snake.append((ny, nx, nd))
                m[ny][nx] = 'S'
                y, x, d = snake.popleft()
            m[y][x] = '.'
            
            # 몸통과 머리가 만나는지 확인
            for i in range(length-1):
                # 머리와 몸통이 만남
                if  next_y == points[i][0] and next_x == points[i][1]:
                    flag = True
                    break
    # 벽이면 게임 끝
    else:
        flag = True
        
    # 머리와 몸통이 만나거나 벽에 박으면 끝
    if flag:
        break
print(count)