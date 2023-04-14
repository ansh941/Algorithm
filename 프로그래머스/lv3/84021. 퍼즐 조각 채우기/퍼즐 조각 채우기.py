from collections import deque

# 상, 하, 좌, 우
dx = [0,0,-1,1]
dy = [-1,1,0,0]

def search_shapes(table, h, w):
    global dx, dy

    visited = [[0 for _ in range(w)] for _ in range(h)]

    shapes = []
    for i in range(h):
        for j in range(w):
            shape = []
            if visited[i][j] == 0 and table[i][j] >= 1:
                y, x = i, j
                q = deque()
                q.append((x,y))
                shape.append([y,x])
                visited[y][x] = 1
                while q:
                    x, y = q.popleft()

                    for k in range(4):
                        next_y = y + dy[k]
                        next_x = x + dx[k]

                        if next_y >= 0 and next_y < h and next_x >= 0 and next_x < w:
                            if table[next_y][next_x] >= 1 and visited[next_y][next_x] == 0:
                                shape.append([next_y, next_x])
                                q.append((next_x,next_y))
                                visited[next_y][next_x] = 1
                shapes.append(shape)
    return shapes

# 테이블 회전
def rotation(table, number):
    new_table = table.copy()
    for i in range(number):
        elements = zip(*new_table[::-1])
        new_table = [list(elem) for elem in elements]

    return new_table

def search_spaces(board, h, w):
    global dx, dy

    visited = [[0 for _ in range(w)] for _ in range(h)]

    spaces = []
    for i in range(h):
        for j in range(w):
            yxs = []
            if visited[i][j] == 0 and board[i][j] == 0:
                y, x = i, j
                q = deque()
                q.append((x,y))
                yxs.append([y, x])
                visited[y][x] = 1
                while q:
                    x, y = q.popleft()

                    for k in range(4):
                        next_y = y + dy[k]
                        next_x = x + dx[k]

                        if next_y >= 0 and next_y < h and next_x >= 0 and next_x < w:
                            if board[next_y][next_x] == 0 and visited[next_y][next_x] == 0:
                                yxs.append([next_y, next_x])
                                q.append((next_x,next_y))
                                visited[next_y][next_x] = 1
                spaces.append(yxs)
    return spaces

def calc_diff(x1, x2, y1, y2):
    return x1-x2, y1-y2

def remove_diff(shape, space):
    shape_y, shape_x = shape[0][0], shape[0][1]
    space_y, space_x = space[0][0], space[0][1]

    diff_x, diff_y = calc_diff(shape_x, space_x, shape_y, space_y)
    for i in range(len(shape)):
        shape[i][0] -= diff_y
        shape[i][1] -= diff_x

    if space == shape:
        return True
    else:
        return False


def fit(shapes, spaces):
    shapes = list(map(list, zip(*shapes)))
    count = 0

    for space in spaces:
        # shape number
        result = None
        for i in range(len(shapes)):
            for rot in shapes[i]:
                if len(rot) == len(space):
                    result = remove_diff(rot, space)
                    if result:
                        count += len(rot)
                        break
            if result:
                del shapes[i]
                break
    return count

def shape_numbering(table, shapes):
    shape_num = 1
    for shape in shapes:
        for num in range(len(shape)):
            y = shape[num][0]
            x = shape[num][1]
            table[y][x] = shape_num
        shape_num+=1
    return table

def solution(game_board, table):
    answer = -1

    all_shapes = []
    shapes = search_shapes(table, len(table), len(table[0]))
    table = shape_numbering(table, shapes)
    all_shapes.append(shapes)

    for i in range(1, 4):
        new_table = rotation(table, i)
        shapes = search_shapes(new_table, len(new_table), len(new_table[0]))
        shapes = sorted(shapes, key=lambda x: new_table[x[0][0]][x[0][1]])
        all_shapes.append(shapes)

    spaces = search_spaces(game_board, len(game_board), len(game_board[0]))

    answer = fit(all_shapes, spaces)

    return answer