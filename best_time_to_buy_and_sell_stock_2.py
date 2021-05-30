class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        size = len(prices)
        if size == 1:
            return 0
        
        def shouldHold(k):
            if k == size - 1 or k == 0:
                return False
            if prices[k] == prices[k+1]:
                return True

        def isPeak(k):
            if k == size - 1:
                return True if prices[k-1] <= prices[k] else False
            if k > 0:
                return True if prices[k] > prices[k + 1] else False
            return False

        def isDip(k):
            if k == 0:
                return True if prices[k + 1] >= prices[k] else False
            if k < size - 1:
                return True if prices[k] < prices[k + 1] else False

        profit = 0
        bought = False
        for i in range(size):
            if shouldHold(i):
                continue
            if isDip(i) and not bought:
                bought = True
                start = i
            if isPeak(i) and bought:
                bought = False
                profit += prices[i] - prices[start]
        return profit
