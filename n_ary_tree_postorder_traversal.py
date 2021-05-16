"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def post_order(self, node):
        if not node:
            return
        for x in node.children:
            self.post_order(x)
        self.arr.append(node.val)

    def postorder(self, root: 'Node') -> List[int]:
        self.arr = []
        self.post_order(root)
        return self.arr
