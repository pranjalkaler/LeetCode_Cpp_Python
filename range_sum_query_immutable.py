class NumArray:

    def __init__(self, nums: List[int]):
        self.sum = [0]
        for i, x in enumerate(nums):
            self.sum.append(self.sum[i] + x)


    def sumRange(self, left: int, right: int) -> int:
        return self.sum[right + 1] - self.sum[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)