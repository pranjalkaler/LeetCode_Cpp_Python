class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        def Sort(Nums):
            for i in range(1, len(Nums)):
                key = Nums[i]
                j = i - 1
                while j >= 0 and key > Nums[j]:
                    Nums[j + 1] = Nums[j]
                    j -= 1
                Nums[j + 1] = key

        total = 0
        for x in nums:
            total += x
        slidingSum = 0
        Sort(nums)
        print(nums, total, slidingSum)
        for i, x in enumerate(nums):
            slidingSum += x
            total -= x
            print(i, x, total, slidingSum)
            if slidingSum > total:
                return nums[:i+1]
            