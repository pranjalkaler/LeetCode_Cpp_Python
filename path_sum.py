# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recur(self, node, target, sum_so_far):
        if not node:
            return False

        if not node.left and not node.right:
            # This is a leaf node
            if node.val + sum_so_far == target:
                return True

        path_in_left = self.recur(node.left, target, sum_so_far + node.val)
        path_in_right = self.recur(node.right, target, sum_so_far + node.val)
        return path_in_left or path_in_right

    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        return self.recur(root, targetSum, 0)