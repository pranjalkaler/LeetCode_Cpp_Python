# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not inorder:
            return None
        while preorder[0] not in inorder:
            preorder.pop(0)
        root = preorder.pop(0)
        index = inorder.index(root)
        left_in = inorder[:index]
        right_in = inorder[index+1:]
        leftNode = self.buildTree(preorder[:], left_in)
        rightNode = self.buildTree(preorder[:], right_in)
        
        node = TreeNode(root, leftNode, rightNode)
        return node
