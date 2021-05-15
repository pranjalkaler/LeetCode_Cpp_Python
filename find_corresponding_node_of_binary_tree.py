# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        queue = [ cloned ]
        while queue:
            levelSize = len(queue)
            for x in range(levelSize):
                left = Right = False
                node = queue.pop(0)
                if node.val == target.val:
                    if node.left and target.left:
                        if node.left.val == target.left.val:
                            return node
                    else:
                        left = True
                    if node.right and target.right:
                        if node.right.val == target.right.val:
                            return node                        
                    else:
                        right = True
                    if left and right:
                        return node
                if node and node.left:
                    queue.append(node.left)
                if node and node.right:
                    queue.append(node.right)
