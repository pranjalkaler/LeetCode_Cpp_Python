# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder:
            return None
        while postorder[-1] not in inorder:
            postorder.pop()
        root = postorder.pop()
        index = inorder.index(root)
        left_in = inorder[:index]
        right_in = inorder[index+1:]
        leftNode = self.buildTree(left_in, postorder[:])
        rightNode = self.buildTree(right_in, postorder[:])
        
        node = TreeNode(root, leftNode, rightNode)
        return node
