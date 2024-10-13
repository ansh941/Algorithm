class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        answer = [[1], [1,1]]

        for i in range(2, numRows):
            new_vec = []
            for j in range(0, i):
                if j == 0:
                    new_vec.append(1)
                elif j < i:
                    new_val = answer[i-1][j-1] + answer[i-1][j]
                    new_vec.append(new_val)
            new_vec.append(1)
            answer.append(new_vec)
            
        return answer[:numRows]