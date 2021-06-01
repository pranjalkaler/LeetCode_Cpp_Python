class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        for i in reversed(range(n-1)):
            for j in range(n):
                cases = []
                if j-1 >= 0:
                    cases.append(matrix[i+1][j-1] + matrix[i][j])
                if j+1 < n:
                    cases.append(matrix[i+1][j+1] + matrix[i][j])
                cases.append(matrix[i+1][j] + matrix[i][j])
                matrix[i][j] = min(cases)
        return min(matrix[0])
