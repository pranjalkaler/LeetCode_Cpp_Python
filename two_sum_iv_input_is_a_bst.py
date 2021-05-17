# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        List = []
        def inOrder(node):
            if not node:
                return
            inOrder(node.left)
            List.append(node.val)
            inOrder(node.right)
        inOrder(root)
        print(List)
        for i in range(len(List)):
            for j in range(i+1, len(List)):
                if List[i] + List[j] == k:
                    return True
        return False