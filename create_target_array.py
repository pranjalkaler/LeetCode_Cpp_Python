class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = []
        # list.insert(index, element)
        for (n, i) in zip(nums, index):
            target.insert(i, n)
        return target