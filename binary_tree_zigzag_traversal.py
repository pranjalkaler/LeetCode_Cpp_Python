# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return root
        queue = [ root ]
        result = []
        depth = 1
        while queue:
            print("*" * 4)
            base = len(queue)
            level = []
            for x in range(base):
                node = queue.pop(0)
                if node:
                    level.append(node.val)
                if node and node.left:
                    queue.append(node.left)
                if node and node.right:
                    queue.append(node.right)
            print(level)
            if depth % 2 == 0:
                level = level[::-1]
            depth += 1
            print(level)
            result.append(level)
            level = []
        print(result)
        return result
            
        