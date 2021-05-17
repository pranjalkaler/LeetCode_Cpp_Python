# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDiff(self, node, ancestors):
        minDiff = 100000
        for ancestor in ancestors:
            minDiff = min(minDiff, abs(ancestor - node.val))
        if not node.left and not node.right:
            # it is a leaf node
            return minDiff
        leftAncestors, rightAncestors = [], []
        leftAncestors.extend(ancestors)
        rightAncestors.extend(ancestors)
        leftAncestors.append(node.val)
        rightAncestors.append(node.val)
        leftMin = rightMin = 100000
        if node.left:
            leftMin = self.getDiff(node.left, leftAncestors)
        if node.right:
            rightMin = self.getDiff(node.right, rightAncestors)
        return min(leftMin, rightMin, minDiff)

    def getMinimumDifference(self, root: TreeNode) -> int:
        return self.getDiff(root, [])