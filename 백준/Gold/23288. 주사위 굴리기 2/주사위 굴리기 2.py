# 세로, 가로, 이동 횟수
N,M,K = map(int, input().split())

map_ = []
for i in range(N):
    map_.append(list(map(int, input().split())))
    

# 주사위 모양
#   2
# 4 1 3
#   5
#   6

def move_north(dice):
    dice[0], dice[2], dice[4], dice[5] = dice[2], dice[4], dice[5], dice[0]
    return dice

def move_south(dice):
    dice[0], dice[2], dice[4], dice[5] = dice[5], dice[0], dice[2], dice[4]
    return dice

def move_east(dice):
    dice[1], dice[2], dice[3], dice[5] = dice[5], dice[1], dice[2], dice[3]
    return dice

def move_west(dice):
    dice[1], dice[2], dice[3], dice[5] = dice[2], dice[3], dice[5], dice[1]
    return dice

# 처음 이동 방향은 동쪽
# 이동 방향으로 한 칸 굴러간다. 칸이 없다면 이동 방향을 반대로 하고 한 칸 굴러간다
# 도착한 칸에 대한 점수를 획득
# 주사위 아랫면의 정수 A와 칸의 정수 B를 비교해 이동 방향을 결정
# A가 크면 이동 방향을 시계 방향 90도 회전
# B가 크면 반시계 90도 회전
# 같으면 변화 없음

# 점수는 다음과 같이 구한다.
# 이동했을 때 도착한 곳의 점수를 B라 할 때, 동서남북으로 연속해서 이동할 수 있는 칸의 수를 C라 한다.
# B*C가 점수가 된다. 이 때 이동할 수 있는 칸은 모두 B여야 한다.

from collections import deque

dice = [2,4,1,3,5,6]

# 이동 방향
dx = [0,0,-1,1]
dy = [-1,1,0,0]

# 주사위 이동
# 동 남 서 북
dice_direction = 0
total_score = 0

# 초기 dice의 위치
x,y = 0,0
for k in range(K):
    # dice 이동
    while True:
        if dice_direction%4 == 0:
            if x+1 < M:
                dice = move_east(dice)
                x += 1
                break
            else:
                dice_direction+=2
        elif dice_direction%4 == 1:
            if y+1 < N:
                dice = move_south(dice)
                y+=1
                break
            else:
                dice_direction+=2
        elif dice_direction%4 == 2:
            if x-1 >= 0:
                dice = move_west(dice)
                x-=1
                break
            else:
                dice_direction+=2
        elif dice_direction%4 == 3:
            if y-1 >= 0:
                dice = move_north(dice)
                y-=1
                break
            else:
                dice_direction+=2
    score = map_[y][x]
    
    q = deque()
    q.append((x,y))
    visited = [[0 for _ in range(M)] for _ in range(N)]
    visited[y][x] = 1
    
    score_count = 1
    while q:
        cur_x, cur_y = q.popleft()
        
        for i in range(4):
            next_x = cur_x + dx[i]
            next_y = cur_y + dy[i]
            
            if next_x >= 0 and next_x < M and next_y >= 0 and next_y < N:
                if map_[next_y][next_x] == score and visited[next_y][next_x] == 0:
                    q.append((next_x, next_y))
                    visited[next_y][next_x] = 1
                    score_count += 1
    
    if dice[-1] > score:
        dice_direction += 1
    elif dice[-1] < score:
        dice_direction -= 1
    total_score += (score * score_count)
print(total_score)