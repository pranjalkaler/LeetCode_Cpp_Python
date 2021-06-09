# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class CBTInserter:

    def __init__(self, root: TreeNode):
        self.tree = root
        self.queue = [self.tree]
        while self.queue:
            node = self.queue[0]
            if node.left == None:
                break
            self.queue.append(node.left)
            if node.right == None:
                break
            self.queue.append(node.right)
            self.queue.pop(0)

    def insert(self, v: int) -> int:
        node = TreeNode(v)
        # print(self.queue[0].val)
        if self.queue[0].left == None:
            self.queue[0].left = node
            self.queue.append(node)
            return self.queue[0].val
        elif self.queue[0].right == None:
            self.queue[0].right = node
            self.queue.append(node)
            reply = self.queue.pop(0)
            return reply.val
            

    def get_root(self) -> TreeNode:
        return self.tree


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(v)
# param_2 = obj.get_root()