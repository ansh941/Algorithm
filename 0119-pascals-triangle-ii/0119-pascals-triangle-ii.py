class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        triangles = [[1], [1,1]]

        for i in range(2, rowIndex+1):
            new_vec = []
            for j in range(0, i):
                if j == 0:
                    new_vec.append(1)
                elif j < i:
                    new_val = triangles[i-1][j-1] + triangles[i-1][j]
                    new_vec.append(new_val)
            new_vec.append(1)
            triangles.append(new_vec)
        return triangles[rowIndex]
            
      