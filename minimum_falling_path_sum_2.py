class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        n = len(arr)
        for i in reversed(range(n-1)):
            for j in range(n):
                Min = 1000
                for k in range(n):
                    if j != k and arr[i][j] + arr[i+1][k] < Min:
                        Min = arr[i][j] + arr[i+1][k]
                arr[i][j] = Min
        return min(arr[0])
