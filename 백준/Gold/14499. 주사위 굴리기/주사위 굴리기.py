# N, M : 지도 크기(세로, 가로)
# x, y : 지도 좌표
# K : 명령의 개수
N, M, x, y, K = map(int, input().split())

m = []
for i in range(N):
    m.append(list(map(int, input().split())))

# 명령
# 동 : 1
# 서 : 2
# 북 : 3
# 남 : 4
order = list(map(int, input().split()))


# 주사위 형태
#   0
# 1 2 3
#   4
#   5

# 동 : 1->2 2->3 3->5 5->1
# 서 : 1->5 2->1 3->2 5->3
# 북 : 0->5 2->0 4->2 5->4
# 남 : 0->2 2->4 4->5 5->0
def roll_dice(dice, direction):
    if direction == 1:
        dice[1], dice[2], dice[3], dice[5] = dice[2], dice[3], dice[5], dice[1]
    elif direction == 2:
        dice[1], dice[2], dice[3], dice[5] = dice[5], dice[1], dice[2], dice[3]
    elif direction == 3:
        dice[0], dice[2], dice[4], dice[5] = dice[5], dice[0], dice[2], dice[4]
    else:
        dice[0], dice[2], dice[4], dice[5] = dice[2], dice[4], dice[5], dice[0]
        
    return dice

dice = [0 for _ in range(6)]

#    동  서  북 남
dx = [0, 0, -1, 1]
dy = [1, -1, 0 ,0]

# 주사위를 굴렸을 때, 이동한 칸에 쓰여있는 수가 0이면 주사위의 바닥면에 쓰여있는 수가 복사
# 0이 아니면 칸에 쓰여있는 수가 주사위의 바닥으로 복사되고 칸에 쓰여있는 수가 0이 된다.
for i in range(K):
    next_y = y+dy[order[i]-1]
    next_x = x+dx[order[i]-1]
    if next_y >= 0 and next_y < M and next_x >= 0 and next_x < N:
        dice = roll_dice(dice, order[i])
        if m[next_x][next_y] == 0:
            m[next_x][next_y] = dice[5]
        else:
            dice[5] = m[next_x][next_y]
            m[next_x][next_y] = 0
        print(dice[2])
        y = next_y
        x = next_x