"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        queue = [ root ]
        result = []
        while queue:
            level = []
            size = len(queue)
            for x in range(size):
                node = queue.pop(0)
                level.append(node.val)
                for y in node.children:
                    queue.append(y)
            result.append(level)
        return result