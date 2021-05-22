class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        Hash = {}
        for x in nums:
            if x in Hash.keys():
                return x
            Hash[x] = True
