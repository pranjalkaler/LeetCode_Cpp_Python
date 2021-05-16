# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node):
        if not node:
            return 0
        leftSum = self.dfs(node.left)
        rightSum = self.dfs(node.right)
        totalSum = node.val + leftSum + rightSum
        node.val = abs(leftSum - rightSum)
        return totalSum

    def findTilt(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        self.dfs(root)

        queue = [ root ]
        tilt = 0
        while queue:
            node = queue.pop(0)
            tilt += node.val
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return tilt