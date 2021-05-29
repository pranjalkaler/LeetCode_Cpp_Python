class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        print(nums)
        print(nums[0], nums[1], nums[-1], nums[-1], nums[-2], nums[-3])
        return max(nums[0]*nums[1]*nums[-1], nums[-1]*nums[-2]*nums[-3])
