class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        count = 0
        freq = { i : 0 for i in range(0, 61) }
        for x in time:
            p = x % 60
            if p == 0:
                count += freq[p]
            else:
                count += freq[60 - p]
            freq[p] += 1
        return count
