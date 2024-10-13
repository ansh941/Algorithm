from collections import deque

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        memo = {}

        q = deque([(triangle[0][0], 0, 0)])
        answer = float('inf')
        while q:
            val, row, col = q.pop()

            if row == len(triangle) - 1:
                answer = min(answer, val)
                continue

            if (row, col) in memo and memo[(row, col)] <= val:
                continue

            memo[(row, col)] = val

            q.append((val + triangle[row + 1][col], row + 1, col))
            q.append((val + triangle[row + 1][col + 1], row + 1, col + 1))

        return answer