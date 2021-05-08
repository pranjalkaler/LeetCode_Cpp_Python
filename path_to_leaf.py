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
        left_list = []
        right_list = []
        main_list = []
        if node.left:
            left_list = self.inOrder(node.left)
            for x in left_list:
                main_list.append("{}|{}".format(node.val, x))
        if node.right:
            right_list = self.inOrder(node.right)
            for x in right_list:
                main_list.append("{}|{}".format(node.val, x))
        return main_list if main_list else [ "{}".format(node.val) ]

    def convertToPath(self, string):
        result = ""
        string = string.split("|")
        for i in range(len(string) - 1):
            result += "{}->".format(string[i])
        result += string[-1]
        return result

    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        List = self.inOrder(root)
        print(List)
        for i in range(len(List)):
            List[i] = self.convertToPath(List[i])
        print(List)
        return List
