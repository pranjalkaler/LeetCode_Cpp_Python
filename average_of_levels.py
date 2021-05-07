# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        queue = [ root ]
        average = [ ]
        while queue:
            size = len(queue)
            lsum = 0
            for i in range(size):
                node = queue.pop(0)
                lsum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            average.append(lsum/size)
        return average