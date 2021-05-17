# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        if not root:
            return "#"
        queue = [ root ]
        result = ""
        while queue:
            node = queue.pop(0)
            if node == "#":
                result += "# "
                continue
            result += "{} ".format(node.val)
            if node.left:
                queue.append(node.left)
            else:
                queue.append("#")
            if node.right:
                queue.append(node.right)
            else:
                queue.append("#")
        result.strip("# ")
        return result

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        def is_int(x):
            try: 
                int(x)
                return True
            except ValueError:
                return False

        if data == "" or data == "#":
            return None
        data = data.split(" ")
        root = TreeNode(data.pop(0))
        queue = [ root ]
        while data:
            left = data.pop(0)
            right = data.pop(0) if len(data) > 0 else "#"
            leftNode = TreeNode(left) if is_int(left) else None
            rightNode = TreeNode(right) if is_int(right) else None
            if len(queue) == 0:
                break
            node = queue.pop(0)
            if leftNode:
                node.left = leftNode
                queue.append(node.left)
            if rightNode:
                node.right = rightNode
                queue.append(node.right)
        return root

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans