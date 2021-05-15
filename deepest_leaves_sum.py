# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = [ root ]
        while queue:
            levelSize = len(queue)
            levelSum = 0
            for x in range(levelSize):
                node = queue.pop(0)
                levelSum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if len(queue) == 0:
                return levelSum
        return 0
