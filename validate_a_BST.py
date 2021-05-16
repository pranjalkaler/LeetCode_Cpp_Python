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
        self.inOrder(node.left)
        self.list.append(node.val)
        self.inOrder(node.right)

    def isValidBST(self, root: TreeNode) -> bool:
        if not root.left and not root.right:
            return [root.val]

        self.list = []
        self.inOrder(root)
        print(self.list)
        if len(self.list) <= 2:
            return self.list[0] < self.list[1]
        for idx in range(1, len(self.list)):
            if self.list[idx - 1] >= self.list[idx]:
                return False
        return True
            