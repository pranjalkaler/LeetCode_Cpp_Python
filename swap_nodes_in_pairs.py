# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        node = head
        while node:
            if node.next:
                temp = node.val
                node.val = node.next.val
                node.next.val = temp
                node = node.next.next
            else:
                break           
        
        return head