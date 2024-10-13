from collections import deque

class Solution:
    def jump(self, nums: List[int]) -> int: 
        idx = len(nums) - 1
        answer = 0
        while idx > 0:
            indices = []
            for i in range(1, idx+1):
                if (idx - i) + nums[idx - i] >= idx:
                    indices.append(idx - i)
            idx = min(indices)
            answer += 1
        return answer