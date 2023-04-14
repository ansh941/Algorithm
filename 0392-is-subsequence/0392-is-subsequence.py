class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if(s==""):
            return True
        
        flag = len(s)
        p = 0
        
        for i in range(len(t)):
            if(t[i] == s[p]):
                flag -= 1
                p+=1
            
            if(flag == 0):
                return True
        return False
                