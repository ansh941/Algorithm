import math
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = int(-math.pow(10,5))
        cur_sum = int(-math.pow(10,5))
        for i in range(len(nums)):
            if(cur_sum < 0):
                cur_sum = nums[i]
            else:
                cur_sum += nums[i]
            if(cur_sum > max_sum):
                max_sum = cur_sum
        return max_sum
        
        
                
        
        