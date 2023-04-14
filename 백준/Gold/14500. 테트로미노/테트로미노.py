N, M = map(int, input().split())

paper = []
for i in range(N):
    paper.append(list(map(int, input().split())))

shapes = [[(0,1), (0,2), (0,3)],
          [(1,0), (2,0), (3,0)],
          [(0,1), (1,0), (1,1)],
          [(1,0), (2,0), (2,1)],
          [(0,1), (0,2), (-1,2)],
          [(0,1), (1,1), (2,1)],
          [(0,1), (0,2), (1,0)],
          [(0,1), (-1,1), (-2,1)],
          [(1,0), (1,1), (1,2)],
          [(0,1), (1,0), (2,0)],
          [(0,1), (0,2), (1,2)],
          [(1,0), (1,1), (2,1)],
          [(0,1), (-1,1), (-1,2)],
          [(-1,0), (-1,1), (-2,1)],
          [(0,1), (1,1), (1,2)],
          [(0,1), (0,2), (1,1)],
          [(0,1), (1,1), (-1,1)],
          [(0,1), (0,2), (-1,1)],
          [(1,0), (1,1), (2,0)]]

maximum = 0
for i in range(N):
    for j in range(M):
        for s in range(len(shapes)):
            flag=True
            val = paper[i][j]
            for k in range(3):
                y = i+shapes[s][k][0]
                x = j+shapes[s][k][1]
                if y >= 0 and y < N and x >= 0 and x < M:
                    val += paper[y][x]
                else:
                    flag = False
                    break
            if flag and maximum < val:
                maximum = val
print(maximum)