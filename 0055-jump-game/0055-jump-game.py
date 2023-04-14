class Solution:
    def canJump(self, nums: List[int], p=0) -> bool:
        if(p >= len(nums)-1):
            return True
        if(nums[p] == 0):
            return False
        
        end = len(nums)
        if(p+nums[p]+1 < len(nums)):
            end = p+nums[p]+1

        max_loc = p+1
        print(end, p, end-p, max_loc)
        for i in range(1,end-p):
            if(max_loc+nums[max_loc] <= p+i+nums[p+i]):
                max_loc = p+i
                
            
            if(max_loc >= len(nums)-1):
                return True
        
        result = False
        result = result or self.canJump(nums, max_loc)
        if(result == True):
            return result
            