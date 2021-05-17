# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        List = []
        def inOrder(node):
            if not node:
                return
            inOrder(node.left)
            List.append(node.val)
            inOrder(node.right)
        inOrder(root)
        MIN = 1000000
        for x in range(1, len(List)):
            diff = abs(List[x - 1] - List[x])
            if diff < MIN:
                MIN = diff
        return MIN