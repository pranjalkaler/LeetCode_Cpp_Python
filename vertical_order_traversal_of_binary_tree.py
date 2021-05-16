# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node, x, y):
        if not node:
            return
        self.dfs(node.left, x+1, y-1)
        if y not in self.dict.keys():
            self.dict[y] = dict()
            self.dict[y][x] = [ node.val ]
        else:
            if x not in self.dict[y].keys():
                self.dict[y][x] = dict()
                self.dict[y][x] = [ node.val ]
            else:
                self.dict[y][x].append(node.val)
        self.dfs(node.right, x+1, y+1)        

    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        self.dict = {}
        self.dfs(root, 0, 0)
        result = []
        for _, v in sorted(self.dict.items(), key=lambda item:item[0]):
            tmp=[]
            for _, v2 in sorted(v.items(),key=lambda item1:item1[0]):
                v2.sort()
                tmp.extend(v2)
            result.append(tmp)
        return result