
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        flag = False
        
        if(needle==""):
            return 0
        
        for i in range(len(haystack)-len(needle)+1):
            for j in range(len(needle)):
                if(haystack[i+j] != needle[j]):
                    flag = False
                    break
                else:
                    flag = True
            if(flag == True):
                return i
        return -1
            