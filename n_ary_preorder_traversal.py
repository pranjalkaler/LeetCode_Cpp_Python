"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
        
    CHILDREN IS A LIST OF NODES
"""

class Solution:
    def __init__(self):
        self.array = []

    def inOrder(self, node):
        if node:
            self.array.append(node.val)
            for x in node.children:
                self.inOrder(x)
        
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return root
        self.inOrder(root)
        print(self.array)
        return self.array
        