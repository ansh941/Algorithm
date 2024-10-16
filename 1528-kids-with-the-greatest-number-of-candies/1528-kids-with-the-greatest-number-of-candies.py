import copy

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        answer = [False for _ in range(len(candies))]

        maximum = max(candies)
        for i in range(len(candies)):
            if maximum <= candies[i] + extraCandies:
                answer[i] = True
        return answer 

