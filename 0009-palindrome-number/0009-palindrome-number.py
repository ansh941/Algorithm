class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        length = len(x)//2+1
        for i in range(length):
            if(x[i] != x[-i-1]):
                return False
        return True