class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        N = len(nums)
        count = 0
        for i in range(N):
            if nums[i] == val:
                count += 1
        for i in reversed(range(0, N-1)):
            if nums[i] == val:
                key = nums[i]
                j = i + 1
                while j <= N - 1 and nums[j] != key:
                    nums[j-1] = nums[j]
                    j += 1
                nums[j-1] = key
        return N - count
