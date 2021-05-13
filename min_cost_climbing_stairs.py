class Solution:
    
    def KS(self, N):
        if N < 2:
            return 0
        if self.arr[N-2] == -1:
            self.arr[N-2] = self.KS(N-2)
        if self.arr[N-1] == -1:
            self.arr[N-1] = self.KS(N-1)
        return min(self.cost[N-1] + self.arr[N-1], self.cost[N-2] + self.arr[N-2])

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        self.cost = cost
        self.arr = [-1] * len(cost)
        return self.KS(len(cost))