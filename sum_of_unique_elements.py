class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        freq = {key: 0 for key in nums }
        print(freq)
        for x in nums:
            freq[x] += 1
        return sum(key for key, val in freq.items() if val == 1)