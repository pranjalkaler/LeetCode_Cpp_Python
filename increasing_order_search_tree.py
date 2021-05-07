# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.array = []

    def inOrder(self, node):
        if node:
            self.inOrder(node.left)
            self.array.append(node.val)
            self.inOrder(node.right)
    
    def createTree(self):
        root = node = TreeNode(self.array[0], left=None)
        for x in range(1, len(self.array)):
            node.right = TreeNode(self.array[x], left=None)
            node = node.right
            print(node)
        return root

    def increasingBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        self.inOrder(root)
        print(self.array)
        return self.createTree()
        
        