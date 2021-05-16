# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDiff(self, node, ancestors):
        maxDiff = 0
        # print("Ancestors for node {}: {}".format(node.val, ancestors))
        for ancestor in ancestors:
            maxDiff = max(maxDiff, abs(ancestor - node.val))
        if not node.left and not node.right:
            # it is a leaf node
            # print("Returning1 {} at {}".format(maxDiff, node.val))
            return maxDiff
        leftAncestors, rightAncestors = [], []
        leftAncestors.extend(ancestors)
        rightAncestors.extend(ancestors)
        leftAncestors.append(node.val)
        rightAncestors.append(node.val)
        leftMax = rightMax = 0
        if node.left:
            leftMax = self.getDiff(node.left, leftAncestors)
        if node.right:
            rightMax = self.getDiff(node.right, rightAncestors)
        
        # print("Returning2 {} at {}".format(max(leftMax, rightMax, maxDiff), node.val))
        return max(leftMax, rightMax, maxDiff)

    def maxAncestorDiff(self, root: TreeNode) -> int:
        return self.getDiff(root, [])