# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        queue = [ root ]
        MaxSum = -10 ** 6
        level = Level = 0
        while queue:
            levelSum = 0
            level += 1
            size = len(queue)
            for x in range(size):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                levelSum += node.val
            if levelSum > MaxSum:
                MaxSum = levelSum
                Level = level
        return Level
    