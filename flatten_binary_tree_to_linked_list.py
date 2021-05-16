# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preOrder(self, node):
        if not node:
            return
        self.list.append(node.val)
        self.preOrder(node.left)
        self.preOrder(node.right)

    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.list = []
        self.preOrder(root)
        node = root
        while self.list:
            if node.left:
                node.left = None
            node.val = self.list.pop(0)
            if len(self.list) > 0:
                if not node.right:
                    node.right = TreeNode()
                node = node.right
        return root
        