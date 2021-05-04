class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = [nums2[-1]]
        size = len(nums2)
        nextNum = [ -1 for x in range(size) ]
        for i in range(size - 2, -1, -1): # start, stop, step
            if nums2[i] < stack[-1]:
                nextNum[i] = stack[-1]
            else:
                while len(stack) > 0 and nums2[i] > stack[-1]:
                    stack.pop()
                if len(stack) != 0:
                    nextNum[i] = stack[-1]
            stack.append(nums2[i])
        print(nextNum)
        
        result = [-1 for x in range(len(nums1))]
        for idx, val in enumerate(nums1):
            result[idx] = nextNum[nums2.index(val)]
        return result