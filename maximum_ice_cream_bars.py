class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        count = 0
        i = 0
        # print(costs)
        while i < len(costs) and coins > 0 and coins >= costs[i]:
            # print(i, costs[i], costs, count)
            coins -= costs[i]
            i += 1
            count += 1
        return count