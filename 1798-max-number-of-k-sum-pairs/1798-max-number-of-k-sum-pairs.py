from collections import Counter
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        counter = Counter(nums)
        answer = 0
        memo = {}
        for key_num in counter.keys():
            if not memo.get(key_num, False):
                if min(counter[key_num], counter[k-key_num]) > 0:
                    if key_num == k/2:
                        answer += (counter[key_num]//2)
                    else:
                        answer += min(counter[key_num], counter[k-key_num])
                    memo[key_num] = True
                    memo[k-key_num] = True
        return answer