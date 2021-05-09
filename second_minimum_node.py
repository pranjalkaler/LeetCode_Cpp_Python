# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sec_min(self, node):
        if not node.left and not node.right:
            # This is a leaf node
            return [node.val, -1]
        common_list = []
        common_list.extend(self.sec_min(node.left))
        common_list.extend(self.sec_min(node.right))
        common_list = list(set(common_list))
        common_list.sort()
        print("#"*10)
        print(common_list)
        print(common_list[0:3])
        return common_list[0:3]

    def findSecondMinimumValue(self, root: TreeNode) -> int:
        l = self.sec_min(root)
        return -1 if len(l) == 2 else l[2]
# ##########
# [5, -1]
# [5, -1]
# ##########
# [5, 2, -1]
# [5, 2]
