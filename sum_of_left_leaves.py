# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node):
        if not node:
            return 0
        if node.left and not node.left.left and not node.left.right:
            self.sum_of_left += node.left.val
        self.dfs(node.left)
        self.dfs(node.right)

    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        self.sum_of_left = 0
        self.dfs(root)
        return self.sum_of_left