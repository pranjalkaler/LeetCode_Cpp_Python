# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        hashmap = {}
        while head:
            key = hex(id(head))
            if key in hashmap.keys():
                return True
            else:
                hashmap[key] = head.val
                head = head.next
            # print(hashmap)
        return False
        