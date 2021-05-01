class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        result = prices
        for idx, val in enumerate(prices):
            if idx < len(prices) - 1:
                j = idx + 1
                while j < len(prices) - 1 and prices[j] > prices[idx]:
                    j += 1
                result[idx] = prices[idx] - prices[j] if prices[j] <= prices[idx] else prices[idx]
        return result