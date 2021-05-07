# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def inOrder(self, node):
        if not node:
            return [ "" ]
        list_of_numbers = []
            
        if node.left:
            left_list = self.inOrder(node.left)
            for x in left_list:
                list_of_numbers.append( "{}{}".format(node.val, x))
        if node.right:
            right_list = self.inOrder(node.right)
            for x in right_list:
                list_of_numbers.append( "{}{}".format(node.val, x))
        if len(list_of_numbers) == 0:
            return [ str(node.val) ]
        else:
            return list_of_numbers
            
    def sumRootToLeaf(self, root: TreeNode) -> int:
        result = 0
        print(self.inOrder(root))
        for x in self.inOrder(root):
            result += int(x, 2)
        return result