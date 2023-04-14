import math

def solution(w,h):
    answer = 1
    
    if w == 1 or h == 1:
        return 0
    elif w == h:
        return w*(h-1)
    else:
        count = 0
        m, M = 0, 0
        for x in range(1,w+1):
            y = h*x/w
            M = math.ceil(y)
            count += abs(M-m)
            
            if y%1 == 0:
                break
            m=M-1
        count *= (w//x)
    answer = (w*h)-count
    return answer