class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for i in reversed(range(len(triangle) - 1)):
            for j in range(len(triangle[i])):
                v1 = triangle[i][j] + triangle[i+1][j]
                v2 = triangle[i][j] + triangle[i+1][j+1]
                triangle[i][j] = min(v1, v2)
        return triangle[0][0]
