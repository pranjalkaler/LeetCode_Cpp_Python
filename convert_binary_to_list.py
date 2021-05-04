# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        number = []
        while head:
            number.append(head.val)
            head = head.next
        size = len(number)
        result = 0
        for i in range(size):
            result += number[size - i - 1] * (2 ** i)
        return result
        