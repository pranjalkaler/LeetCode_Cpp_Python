class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        result = [ 0 for i in range(len(nums))]
        for i in range(len(nums)):
            if i == 0:
                result[i] = nums[i]
            else:
                if nums[i] > nums[i-1]:
                    result[i] = result[i-1] + nums[i]
                else:
                    result[i] = nums[i]
        return max(result)
