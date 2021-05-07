# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        queue = [ root ]
        result = []
        while queue:
            base = len(queue)
            for x in range(base):
                # print("Inside for, x = {}, queue = {}".format(x, len(queue)))
                node = queue.pop(0)
                if node and x == base - 1:
                    result.append(node.val)
                if node and node.left:
                    queue.append(node.left)
                if node and node.right:
                    queue.append(node.right)
                # print(result)
        return result
                    