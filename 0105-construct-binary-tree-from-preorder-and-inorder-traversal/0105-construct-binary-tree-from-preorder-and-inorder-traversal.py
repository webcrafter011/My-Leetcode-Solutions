# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder, inorder):
        in_map = {val: idx for idx, val in enumerate(inorder)}

        def helper(pre_start, pre_end, in_start, in_end):
            if pre_start > pre_end or in_start > in_end:
                return None

            root_val = preorder[pre_start]
            root = TreeNode(root_val)

            in_root = in_map[root_val]
            nums_left = in_root - in_start

            root.left = helper(pre_start + 1, pre_start + nums_left, in_start, in_root - 1)
            root.right = helper(pre_start + nums_left + 1, pre_end, in_root + 1, in_end)

            return root

        return helper(0, len(preorder) - 1, 0, len(inorder) - 1)
