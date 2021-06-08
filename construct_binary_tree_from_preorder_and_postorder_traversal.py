# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        if len(pre) == 0 or len(post) == 0:
            return None
        root = TreeNode(pre.pop(0))
        if len(pre) == 0:
            return root
        
        count = 0
        left_sub_tree_post = []
        right_sub_tree_post = []
        
        while post[0] != pre[0]:
            left_sub_tree_post.append(post.pop(0))
        left_sub_tree_post.append(post.pop(0))
        while post[0] != root.val:
            right_sub_tree_post.append(post.pop(0))

        left_sub_tree_pre = []
        right_sub_tree_pre = []
        for x in pre:
            if x in left_sub_tree_post:
                left_sub_tree_pre.append(x)
            if x in right_sub_tree_post:
                right_sub_tree_pre.append(x)
        
        root.left = self.constructFromPrePost(left_sub_tree_pre, left_sub_tree_post)
        root.right = self.constructFromPrePost(right_sub_tree_pre, right_sub_tree_post)
        return root
