# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inOrder(self, node, listNo):
        if not node:
            return
        self.inOrder(node.left, listNo)
        self.lists[listNo].append(node.val)
        self.inOrder(node.right, listNo)
    
    def merge(self):
        list1 = self.lists[0]
        list2 = self.lists[1]
        l1 = l2 = 0
        L1, L2 = len(list1), len(list2)
        result = []
        while l1 < L1 or l2 < L2:
            if l1 < L1:
                n1 = list1[l1]
            else:
                n1 = None
            if l2 < L2:
                n2 = list2[l2]
            else:
                n2 = None
            if n1 is not None and n2 is not None:
                if n1 <= n2:
                    result.append(n1)
                    l1 += 1
                else:
                    result.append(n2)
                    l2 += 1
            elif n1 is None:
                result.append(n2)
                l2 += 1
            elif n2 is None:
                result.append(n1)
                l1 += 1
        return result

    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        self.lists = [ [], [] ]
        self.inOrder(root1, 0)
        self.inOrder(root2, 1)
        result = self.merge()
        print(result)
        return result
        

        