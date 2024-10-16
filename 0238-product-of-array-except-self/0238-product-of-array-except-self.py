class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        
        c = 1
        for i in range(len(nums)):
            answer.append(c)
            c *= nums[i]
        print(answer)
        
        c = 1
        for i in range(len(nums)-1, -1, -1):
            answer[i] *= c
            c *= nums[i]

        return answer