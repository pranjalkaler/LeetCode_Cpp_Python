# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invert(self, root):
        if not root:
            return
        self.invert(root.left)
        self.invert(root.right)
        temp = root.left
        root.left = root.right
        root.right = temp

    def invertTree(self, root: TreeNode) -> TreeNode:
        self.invert(root)
        return root