import numpy as np

def calc_crosspoint(f1, f2):
    AD_BC = f1[0]*f2[1] - f1[1]*f2[0]
    
    if AD_BC == 0:
        return 1.1, 1.1
    
    BF_ED = f1[1]*f2[2] - f1[2]*f2[1]
    EC_AF = f1[2]*f2[0] - f1[0]*f2[2]
    
    x = BF_ED / AD_BC
    y = EC_AF / AD_BC
    return x, y
    
def solution(line):
    c_points = set()
    for i in range(len(line)-1):
        for j in range(i+1, len(line)):
            x, y = calc_crosspoint(line[i], line[j])
            if x%1 == 0 and y%1 == 0:
                c_points.add((int(x),int(y)))
    c_points = list(c_points)
    
    maximum = np.max(c_points,0)
    minimum = np.min(c_points,0)
    x_range = maximum[0] - minimum[0] + 1
    y_range = maximum[1] - minimum[1] + 1
    
    answer = [['.' for _ in range(x_range)] for _ in range(y_range)]
    for x,y in c_points:
        x = abs(x - minimum[0])
        y = abs(y - maximum[1])
        answer[y][x] = '*'
    
    for idx in range(len(answer)):
        answer[idx] = ''.join(answer[idx])
    return answer