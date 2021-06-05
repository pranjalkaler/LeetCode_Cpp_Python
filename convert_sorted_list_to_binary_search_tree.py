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
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        print(nums)
        def createTree(arr):
            if len(arr) == 0:
                return None
            if len(arr) == 1:
                return TreeNode(arr[0])
            if len(arr) == 2:
                left = TreeNode(arr[0])
                right = TreeNode(arr[1])
                node = right
                node.left = left
            else:
                mid = int(len(arr)/2)
                left = createTree(arr[:mid])
                right = createTree(arr[mid+1:])
                node = TreeNode(arr[mid], left, right)
            return node

        return createTree(nums)
