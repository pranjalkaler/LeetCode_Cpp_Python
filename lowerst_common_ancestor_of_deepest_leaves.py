# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getPath(self, node, val):
        if not node:
            return []
        if node.val == val:
            return [ node ]
        left = self.getPath(node.left, val)
        if not left:
            right = self.getPath(node.right, val)
            if not right:
                return []
            else:
                path = [ node ]
                path.extend(right)
                return path
        else:
            path = [ node ]
            path.extend(left)
            return path

    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        queue = [ root ]
        deepestNodess = []
        while queue:
            localLevelSize = len(queue)
            deepestNodes = []
            for i in range(localLevelSize):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                deepestNodes.append(node)
        
        paths = []
        for x in deepestNodes:
            paths.append(self.getPath(root, x.val))
        first = last = root
        flag = False
        for i in range(len(paths[0])):
            for j in range(len(paths)):
                if j == 0:
                    first = paths[j][i]
                else:
                    if paths[j][i].val != first.val:
                        flag = True
            if flag:
                return last
            last = first
        return last