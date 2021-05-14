class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        if nums[0] != 0:
            return 0
        size = len(nums)
        for i in range(1, size):
            if nums[i-1] == nums[i] - 1:
                print(nums[i])
            else:
                return i
        return size