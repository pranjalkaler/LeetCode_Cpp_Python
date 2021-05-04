class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        original_size = len(nums)
        nums = nums + nums[0:-1]
        stack = [nums[-1]]
        size = len(nums)
        result = [-1 for x in range(size)]
        for i in range(size - 2, -1, -1):
            while len(stack) > 0 and nums[i] >= stack[-1]:
                stack.pop()
            if len(stack) == 0:
                stack.append(nums[i])
            else:
                result[i] = stack[-1]
                stack.append(nums[i])
        print(result)
        return result[0 : original_size]
        
        