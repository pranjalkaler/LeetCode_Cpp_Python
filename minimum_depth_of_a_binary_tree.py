# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
#     def findDepth(self, node, depth_so_far):
        

    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = [ root ]
        depth = 0
        while queue:
            size = len(queue)
            while size:
                node = queue.pop(0)
                if not node.left and not node.right:
                    # This is a leaf node
                    return depth + 1
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                size -= 1
            depth += 1