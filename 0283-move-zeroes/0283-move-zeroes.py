class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        if len(nums) > 1 and 0 in nums:
            zero_count = nums.count(0)
            zero_idx = nums.index(0)
            nonzero_idx = zero_idx + 1
            while zero_idx < len(nums)-zero_count:
                if nums[nonzero_idx] != 0:
                    nums[zero_idx], nums[nonzero_idx] = nums[nonzero_idx], nums[zero_idx]
                    zero_idx += 1
                nonzero_idx += 1
