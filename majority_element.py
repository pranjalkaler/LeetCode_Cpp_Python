class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return nums[0]
        freq = {}
        size = len(nums)
        for x in nums:
            if x not in freq.keys():
                freq[x] = 1
            else:
                freq[x] += 1
                if freq[x] > int(size/2):
                    return x