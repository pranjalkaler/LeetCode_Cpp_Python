class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        s = 0
        if n % 2 != 0:
            s -= mat[int(n/2)][int(n/2)]
        for i in range(n):
            for j in range(n):
                if i == j:
                    s += mat[i][j]
                if i + j == n - 1:
                    s += mat[i][j]
        return s
