class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum = 0
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                sum = nums[i]
                sum += nums[j]
                if(sum == target):
                    return [i, j]
                
                
                