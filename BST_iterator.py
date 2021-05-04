# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        self.order = []
        self.it = 0
        node = root
        while True:
            if node:
                self.stack.append(node)
                node = node.left
            elif len(self.stack) > 0:
                node = self.stack.pop()
                self.order.append(node.val)
                node = node.right
            else:
                break

    def next(self) -> int:
        self.it += 1
        return self.order[self.it - 1]

    def hasNext(self) -> bool:
        return True if len(self.order) - self.it > 0 else False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()