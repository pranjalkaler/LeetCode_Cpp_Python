# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inOrder(self, node1, node2):
        if not node1 and not node2:
            return None
        _sum = 0
        _sum += node1.val if node1 else 0
        _sum += node2.val if node2 else 0
        current_node = TreeNode(_sum)
        left1 = left2 = right1 = right2 = None
        if node1:
            left1 = node1.left
            right1 = node1.right
        if node2:
            left2 = node2.left
            right2 = node2.right
        current_node.left = self.inOrder(left1, left2)
        current_node.right = self.inOrder(right1, right2)
        return current_node

    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if not root1 and not root2:
            return root1
        elif not root1 and root2:
            return root2
        elif root1 and not root2:
            return root1
        return self.inOrder(root1, root2)
        
        