# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getNumbers(self, node):
        if not node:
            return [""]

        list_of_numbers = []
        if node.left:
            left_numbers = self.getNumbers(node.left)
            for x in left_numbers:
                list_of_numbers.append("{}{}".format(node.val, x))
        if node.right:
            right_numbers = self.getNumbers(node.right)
            for x in right_numbers:
                list_of_numbers.append("{}{}".format(node.val, x))
        
        if len(list_of_numbers) == 0:
            list_of_numbers.append("{}".format(node.val))
        
        return list_of_numbers
            

    def sumNumbers(self, root: TreeNode) -> int:
        numbers = self.getNumbers(root)
        S = 0
        for x in numbers:
            S += int(x)
        return S