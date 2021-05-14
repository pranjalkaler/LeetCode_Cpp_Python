class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxArr = [nums[0]]
        maxPos = maxSum = 0
        for i, x in enumerate(nums):
            if i != 0:
                maxArr.append(max(x + maxArr[i - 1], x))
        return max(maxArr)