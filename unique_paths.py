class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        t = [ [ 1 for i in range(n)] for j in range(m)]
        print(t)
        
        for i in range(1, m):
            for j in range(1, n):
                t[i][j] = t[i-1][j] + t[i][j-1]
        return t[m-1][n-1]
