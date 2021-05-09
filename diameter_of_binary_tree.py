# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDepth(self, root):
        if not root:
            return 0
        # if not root.left and not root.right:
        #     return level
        
        return 1 + max(self.findDepth(root.left), self.findDepth(root.right))
    
    def diameter(self, root):
        if not root:
            return 0
        
        left = self.findDepth(root.left)
        right = self.findDepth(root.right)
        
        ld = self.diameter(root.left)
        rd = self.diameter(root.right)
        return max(left + right + 1, max(ld, rd))
        

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        dia = self.diameter(root)
        print(dia)
        return dia - 1