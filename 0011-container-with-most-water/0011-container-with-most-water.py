class Solution:
    def maxArea(self, height: List[int]) -> int:
        answer = 0
        x1, x2 = 0, len(height)-1
        while x1 < x2:
            x = min(height[x1], height[x2])
            y = x2-x1

            if answer < x * y:
                answer = x * y
            
            if height[x1] < height[x2]:
                x1 += 1
            else:
                x2 -= 1
            
        return answer