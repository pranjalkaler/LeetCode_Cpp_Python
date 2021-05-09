# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        queue = [ root ]
        level = 1
        xh = yh = -1
        while queue:
            size = len(queue)
            while size:
                node = queue.pop(0)
                children = []
                if node.left:
                    children.append(node.left.val)
                    queue.append(node.left)
                if node.right:
                    children.append(node.right.val)
                    queue.append(node.right)
                if x in children and y in children:
                    return False
                if x in children:
                    xh = level
                if y in children:
                    yh = level
                size -= 1
            level += 1
        return True if xh == yh else False
                