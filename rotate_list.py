# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next:
            return head
        length = 0
        node = head
        while node:
            length += 1
            node = node.next
        print(length)
        right_rotations = k % length
        left_rotations = length - right_rotations
        
        last = head
        while last.next:
            last = last.next
        print(last.val)
        
        while left_rotations:
            front = head
            head = head.next
            front.next = None
            last.next = front
            last = front
            left_rotations -= 1
        return head
