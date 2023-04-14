class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        mid = len(nums)//2
        
        if(len(nums) == 1):
            if(nums[mid] < target):
                return mid+1
            else:
                return mid
        
        if(nums[mid] > target):
            return self.searchInsert(nums[:mid], target)
        elif(nums[mid] < target):
            return mid + self.searchInsert(nums[mid:], target)
        else:
            return mid