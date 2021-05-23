class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even = [ x for x in nums if x % 2 == 0 ]
        odd = [ x for x in nums if x % 2 == 1 ]
        e = 0
        o = 0
        for x in range(len(nums)):
            if x % 2 == 0:
                nums[x] = even[e]
                e += 1
            else:
                nums[x] = odd[o]
                o += 1
        return nums
