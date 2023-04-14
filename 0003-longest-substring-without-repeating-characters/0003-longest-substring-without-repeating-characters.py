class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if(s == ""):
            return 0
        
        max_length = 1
        for i in range(len(s)-1):
            length = 1
            for j in range(i+1,len(s)):
                try:
                    p = s[i:j].index(s[j])
                    break
                except:
                    length+=1
            if(length > max_length):
                max_length = length
        return max_length