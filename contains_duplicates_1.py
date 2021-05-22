class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dcx = {}
        for x in nums:
            if x in dcx.keys():
                return True
            dcx[x] = True
        return False