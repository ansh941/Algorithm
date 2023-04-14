# 1,4,7 => left
# 3,6,9 => right
# 2,5,8,0 => near

# pad = [['1','2','3'], 
#        ['4','5','6'], 
#        ['7','8','9'], 
#        ['*','0','#']]
def calc_dist(lp, rp, np, hand):
    ld = abs(lp[0]-np[0]) + abs(lp[1]-np[1])
    rd = abs(rp[0]-np[0]) + abs(rp[1]-np[1])
    
    if(ld > rd):
        h = 'R'
    elif(ld < rd):
        h = 'L'
    else:
        h = hand[0].upper()
    return h

def solution(numbers, hand):

    answer = ''
    lp, rp = (3,0), (3,2)
    
    for i in range(len(numbers)):
        if(numbers[i] % 3 == 1):
            answer += 'L'
            lp = (numbers[i]//3,0)
        elif(numbers[i] % 3 == 0 and numbers[i] != 0):
            answer += 'R'
            rp = (numbers[i]//3-1,2)
        else:
            if(numbers[i] == 0):
                nx = 3
            else:
                nx = numbers[i]//3
            np = (nx, 1)
            h = calc_dist(lp, rp, np, hand)
            if(h=='L'):
                lp = np
            else:
                rp = np
            answer += h
    return answer