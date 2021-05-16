# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getGrandChildren(self, node):
        grandChildren = []
        if node.left:
            if node.left.left:
                grandChildren.append(node.left.left)
            if node.left.right:
                grandChildren.append(node.left.right)
        if node.right:
            if node.right.left:
                grandChildren.append(node.right.left)
            if node.right.right:
                grandChildren.append(node.right.right)
        return grandChildren
        

    def sumEvenGrandparent(self, root: TreeNode) -> int:
        if not root:
            return 0

        queue = [ root ]
        gSum = 0
        
        while queue:
            node = queue.pop(0)
            if node.val % 2 == 0:
                grandChildren = self.getGrandChildren(node)
                for x in grandChildren:
                    gSum += x.val
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return gSum