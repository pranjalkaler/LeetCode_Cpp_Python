class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        result = []
        for freq, val in zip(nums[0::2], nums[1::2]):
            temp = [val]*freq
            result.extend(temp)
        return result
            
        