# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: TreeNode) -> bool:
        def level_in_order(nodes, level):
            if len(nodes) <= 1:
                return True
            for i in range(1, len(nodes)):
                if level % 2 != 0:
                    if nodes[i-1] <= nodes[i] or abs(nodes[i-1] - nodes[i]) % 2 != 0:
                        return False
                else:
                    if nodes[i-1] >= nodes[i] or abs(nodes[i-1] - nodes[i]) % 2 != 0:
                        return False
            return True
        
        queue = [ root ]
        level = -1
        
        while queue:
            level += 1
            levelSize = len(queue)
            levelNodes = []
            for i in range(levelSize):
                node = queue.pop(0)
                levelNodes.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if not level_in_order(levelNodes, level):
                return False
            if (level % 2 == 0 and levelNodes[0] % 2 == 0) or\
               (level % 2 != 0 and levelNodes[0] % 2 != 0):
                return False
        return True