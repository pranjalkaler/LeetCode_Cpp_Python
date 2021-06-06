class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        for i in reversed(range(0, N-1)):
            if nums[i] == 0:
                key = nums[i]
                j = i + 1
                while j <= N - 1 and nums[j] != key:
                    nums[j-1] = nums[j]
                    j += 1
                nums[j-1] = key
