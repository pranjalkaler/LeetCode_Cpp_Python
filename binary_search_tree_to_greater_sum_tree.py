# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inOrder(self, node):
        if not node:
            return
        self.inOrder(node.right)
        self.list.append(node)
        self.inOrder(node.left)

    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.list = []
        self.inOrder(root)
        for i, node in enumerate(self.list):
            if i > 0:
                node.val += self.list[i-1].val
        return root
        
        totalSum = self.func(root, 0)
        return root