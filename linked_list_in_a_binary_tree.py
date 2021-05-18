# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        heads = []
        def isList(node, x)
            if not node:
                return True
            if node and not x:
                return False
            if node.val == x.val:
                return isList(node.next, x.left) or isList(node.next, x.right)
            return False
            
        def getNode(node):
            if not node:
                return
            getNode(node.left)
            getNode(node.right)
            if node.val == head.val:
                heads.append(node)
        getNode(root)
        for x in heads:
            node = head
            if isList(node, x):
                return True
        return False