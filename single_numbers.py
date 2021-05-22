class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        Hash = {}
        for x in nums:
            Hash[x] = Hash[x] + 1 if x in Hash.keys() else 1
        for idx, val in Hash.items():
            if val == 1:
                return idx
