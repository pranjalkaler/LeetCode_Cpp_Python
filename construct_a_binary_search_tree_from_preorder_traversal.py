# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        inOrder = sorted(preorder)
        def binarySearch(arr, key):
            i = 0
            j = len(arr) - 1
            while i <= j:
                mid = i + int((j - i) / 2)
                if arr[mid] == key:
                    return mid
                if arr[mid] > key:
                    j = mid - 1
                else:
                    i = mid + 1
            return -1
        
        def createTree(pO, iO):
            if not pO or not iO:
                return None
            root = TreeNode(pO[0])
            rootIdx = binarySearch(iO, pO[0])
            root.left = createTree(pO[1:rootIdx+1], iO[0:rootIdx])
            root.right = createTree(pO[rootIdx+1:len(iO)], iO[rootIdx+1:len(iO)])
            return root
        return createTree(preorder, inOrder)
            