# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        def getHeight(node, level=0):
            left = right = 0
            if node.left:
                left = getHeight(node.left, level+1)
            if node.right:
                right = getHeight(node.right, level+1)
            return max(level, left, right)
        
        def checkBalance(node):
            if not node:
                return True
            left = right = 0
            if node.left:
                left = getHeight(node.left) + 1
            if node.right:
                right = getHeight(node.right) + 1
            if abs(left - right) > 1:
                return False
            return checkBalance(node.left) and checkBalance(node.right)
        
        return checkBalance(root)