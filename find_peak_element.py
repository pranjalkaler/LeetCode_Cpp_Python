class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        def isPeak(idx):
            if idx == 0 or idx == len(nums) - 1:
                return False
            return nums[idx - 1] < nums[idx] and nums[idx] > nums[idx + 1]

        left = 0
        right = len(nums) - 1
        while left < right:
            mid = int((left + right) / 2)
            # print(left, right, mid)
            if isPeak(mid):
                return mid
            if nums[mid] < nums[mid + 1]:
                # a peak is on right side
                left = mid + 1
            else:
                # a peak is on left side
                right = mid - 1
        return left if nums[left] > nums[right] else right
