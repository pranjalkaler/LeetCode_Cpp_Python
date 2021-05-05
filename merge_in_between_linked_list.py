# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        node1 = list1
        while a - 1 > 0:
            node1 = node1.next
            a -= 1
        
        node2 = list1
        while b:
            node2 = node2.next
            b -= 1
        
        last = list2
        while last.next:
            last = last.next

        node1.next = list2
        last.next = node2.next
        return list1