def solution(rows, columns, queries):
    answer = []
    
    m = []
    num = 1
    for i in range(rows):
        cols = []
        for j in range(columns):
            cols.append(num)
            num+=1
        m.append(cols)
    
    # 우,하,좌,상
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    
    for q in queries:
        tmp = [[m[i][j] for j in range(q[1]-1, q[3])] for i in range(q[0]-1, q[2])]
        
        x_move = q[3]-q[1]
        y_move = q[2]-q[0]
        moving = [x_move,y_move,x_move,y_move]
        
        y_sync = q[0]-1
        x_sync = q[1]-1
        
        y = q[0]-1
        x = q[1]-1
        minimum = tmp[0][0]
        
        for idx, mov in enumerate(moving):
            for _ in range(mov):
                next_y = y+dy[idx]
                next_x = x+dx[idx]
                
                m[next_y][next_x] = tmp[y-y_sync][x-x_sync]
                y = next_y
                x = next_x
                if m[next_y][next_x] < minimum:
                    minimum = m[next_y][next_x]
        answer.append(minimum)
        
    return answer