# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        rootStack = []
        while head:
            rootStack.append(head.val)
            head = head.next
        rootStack = rootStack[::-1]
        print(rootStack)
        size = len(rootStack)
        
        stack = [rootStack[0]]
        result = [0 for x in range(size)]
        for i in range(1, size):
            while len(stack) > 0 and rootStack[i] >= stack[-1]:
                stack.pop()
            if len(stack) == 0:
                stack.append(rootStack[i])
            else:
                result[i] = stack[-1]
                stack.append(rootStack[i])
        return result[::-1]