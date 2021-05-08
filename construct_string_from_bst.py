# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inOrder(self, root):
        if not root:
            return ""
        if not root.left and not root.right:
            return str(root.val)
        
        curr = str(root.val)
        curr += "({})".format(self.inOrder(root.left))
        if root.right:
            curr += "({})".format(self.inOrder(root.right))
        return curr

    def tree2str(self, root: TreeNode) -> str:
        result = self.inOrder(root)
        print(result)
        return result
