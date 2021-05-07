# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def get_leaf_list(self, root):
        stack = [ root ]
        leaf_list = []
        while stack:
            node = stack.pop()
            if not node.left and not node.right:
                leaf_list.append(node.val)
            else:
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
        return leaf_list

    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        leaves_1 = self.get_leaf_list(root1)
        leaves_2 = self.get_leaf_list(root2)
        if len(leaves_1) != len(leaves_2):
            return False
        for i in range(len(leaves_1)):
            if leaves_1[i] != leaves_2[i]:
                return False
        return True