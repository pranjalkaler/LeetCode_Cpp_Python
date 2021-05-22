class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        result = [ -1 ] * len(nums)
        i = 0
        j = len(nums) - 1
        for x in nums:
            if x % 2 == 0:
                result[i] = x
                i += 1
            else:
                result[j] = x
                j -= 1
        return result