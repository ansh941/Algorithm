from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        mc = count.most_common()
        l = list()
        for i in range(len(mc)):
            if(mc[i][1] > (len(nums)/3)):
                l.append(mc[i][0])
        return l