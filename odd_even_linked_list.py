# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        l1 = head
        l2 = h2 = ListNode(-1)
        while True:
            if l1.next:
                l2.next = ListNode(l1.next.val)
                l2 = l2.next
            else:
                l1.next = h2.next
                break
            if l1.next.next:
                l1.next = l1.next.next
            else:
                l1.next = h2.next
                break
            l1 = l1.next
        return head