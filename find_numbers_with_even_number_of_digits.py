class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        def countDigits(num):
            count = 0
            while num:
                digit = num % 10
                num = int(num / 10)
                count += 1
            return count
        
        result = 0
        for num in nums:
            result = result + 1 if countDigits(num) % 2 == 0 else result
        return result
