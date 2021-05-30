class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        size = len(prices)
        if size <= 1:
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

        minPrice = 1000000
        _ = __ = 0
        maxPrice = -1
        maxProfit = -1
        for i in range(size):
            if shouldHold(i):
                continue
            if isDip(i):
                if prices[i] < minPrice:
                    maxProfit = max(maxProfit, prices[__] - prices[_])
                    minPrice = prices[i]
                    _ = i
                    __ = i
                    maxPrice = prices[i]
            if isPeak(i):
                if prices[i] > maxPrice and _ < i and minPrice < prices[i]:
                    maxPrice = prices[i]
                    __ = i
        return max(maxProfit, prices[__] - prices[_])
