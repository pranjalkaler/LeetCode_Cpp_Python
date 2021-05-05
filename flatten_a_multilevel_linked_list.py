"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        stack = []
        node = head
        while node:
            if node.child:
                if node.next:
                    stack.append(node.next)
                node.next = node.child
                node.next.prev = node
                node.child = None
            elif not node.next: # reached end of a subList
                if not stack:
                    break
                temp = stack.pop()
                node.next = temp
                temp.prev = node
            node = node.next
        return head
        