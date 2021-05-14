class Solution:
    def isValid(self, nums):
        if nums[0] + nums[1] > nums[2] and\
           nums[1] + nums[2] > nums[0] and\
           nums[2] + nums[0] > nums[1]:
            return True
        return False

    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        while len(nums) >2:
            tri = nums[-3:]
            if self.isValid(tri):
                return sum(tri)
            else:
                nums.pop()
        return 0
        