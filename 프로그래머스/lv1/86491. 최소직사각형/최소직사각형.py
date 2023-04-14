import numpy as np

def solution(sizes):
    answer = 0
    for i in range(len(sizes)):
        sizes[i] = list(sorted(sizes[i]))
    
    maxes = np.max(sizes, 0)
    answer = int(maxes[0] * maxes[1])
    return answer