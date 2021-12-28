class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        zero_count = 0
        for x in nums:
            if x == 0:
                zero_count = zero_count + 1
            else:
                prod = prod * x
        if zero_count > 1:
            result = [ 0 ] * len(nums)
            print(len(nums))
            print(result)
            return result

        if zero_count == 1:
            result = list()
            for i in range(len(nums)):
                if nums[i] != 0:
                    result.append(0)
                else:
                    result.append(prod)
            return result

        result = list()
        for i in range(len(nums)):
            result.append(int(prod/nums[i]))
        return result
