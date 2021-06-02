class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                top = 200
                left = 200
                if i - 1 >= 0:
                    top = grid[i-1][j]
                if j - 1 >= 0:
                    left = grid[i][j-1]
                grid[i][j] = min(top + grid[i][j], left + grid[i][j])
        return grid[m-1][n-1]
