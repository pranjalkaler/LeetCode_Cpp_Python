# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:    
    def findMode(self, root: TreeNode) -> List[int]:
        queue = [ root ]
        freq = {}
        while queue:
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            if node.val not in freq.keys():
                freq[node.val] = 1
            else:
                freq[node.val] += 1
        print(freq)
        result = []
        maxFreq = 0
        for idx, val in freq.items():
            if maxFreq < val:
                result.clear()
                maxFreq = val
                result.append(idx)
            elif maxFreq == val:
                result.append(idx)
        print(result)
        return result
                