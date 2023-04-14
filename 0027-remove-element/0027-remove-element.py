from collections import Counter

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        length = Counter(nums)[val]
        for i in range(length):
            nums.remove(val)
        return len(nums)