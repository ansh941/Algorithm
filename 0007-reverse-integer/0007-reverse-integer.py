import math

class Solution:
    def reverse(self, x: int) -> int:
        # print(-math.pow(2,31))
        if(x >= math.pow(2,31)-1 or x <= -math.pow(2,31)):
            return 0
        
        r = ''.join(reversed(str(x)))
        if(x<0):
            r = -int(r[:-1])
        else:
            r =  int(r)
        r <= -math.pow(2,31)
        if(r >= math.pow(2,31)-1 or r <= -math.pow(2,31)):
            return 0
        
        return r
            
        
        
    
        
            