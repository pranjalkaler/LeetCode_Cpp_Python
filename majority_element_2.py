class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums
        if len(nums) == 2:
            if nums[0] == nums[1]:
                return [nums[0]]
            return nums
        freq = {}
        size = len(nums)
        result = []
        for x in nums:
            if x not in freq.keys():
                freq[x] = 1
            else:
                freq[x] += 1
                if freq[x] > int(size/3):
                    if x not in result:
                        result.append(x)
        return result
            