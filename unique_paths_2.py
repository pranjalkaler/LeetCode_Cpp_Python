class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        for i in range(row):
            for j in range(col):
                obstacleGrid[i][j] = -1 if obstacleGrid[i][j] == 1 else 0
        found = False
        for j in range(col):
            if obstacleGrid[0][j] != -1:
                obstacleGrid[0][j] = 1
            else:
                break

        found = False
        for i in range(row):
            if obstacleGrid[i][0] != -1:
                obstacleGrid[i][0] = 1
            else:
                break
        print(obstacleGrid)
        for i in range(1, row):
            for j in range(1, col):
                if obstacleGrid[i][j] != -1:
                    top = obstacleGrid[i-1][j] if obstacleGrid[i-1][j] != -1 else 0
                    left = obstacleGrid[i][j-1] if obstacleGrid[i][j-1] != -1 else 0
                    obstacleGrid[i][j] = top + left

        return obstacleGrid[row - 1][col - 1] if obstacleGrid[row - 1][col - 1] != -1 else 0
