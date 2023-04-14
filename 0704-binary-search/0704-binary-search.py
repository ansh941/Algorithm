class Solution:
    def search(self, nums: List[int], target: int) -> int:
        try:
            loc = nums.index(target)
            return loc
        except:
            return -1