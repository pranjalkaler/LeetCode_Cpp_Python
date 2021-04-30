# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        sum = 0
        if root is None:
            return 0
        if root.val >= low and root.val <= high:
            sum += root.val + self.rangeSumBST(root.right, low, high) + self.rangeSumBST(root.left, low, high)
        if root.val < low:
            sum += self.rangeSumBST(root.right, low, high)
        if root.val > high:
            sum += self.rangeSumBST(root.left, low, high)
        return sum