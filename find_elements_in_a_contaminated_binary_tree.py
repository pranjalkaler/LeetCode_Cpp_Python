# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:
    def __init__(self, root: TreeNode):
        self.map = []
        if root:
            root.val = 0
            queue = [ root ]
            while queue:
                node = queue.pop(0)
                self.map.append(node.val)
                if node.left:
                    node.left.val = 2 * node.val + 1
                    queue.append(node.left)
                if node.right:
                    node.right.val = 2 * node.val + 2
                    queue.append(node.right)
        print(self.map)

    def find(self, target: int) -> bool:
        return target in self.map

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)