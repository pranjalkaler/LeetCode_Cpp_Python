class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        rotations_required = k % len(nums)
        while rotations_required:
            last = nums.pop()
            nums.insert(0, last)
            rotations_required -= 1
