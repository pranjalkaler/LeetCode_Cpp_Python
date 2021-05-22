class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])
        
        result = [[-1 for x in range(m)] for y in range(n)]
        print(result)
        for i in range(m):
            for j in range(n):
                result[j][i] = matrix[i][j]
        return result
