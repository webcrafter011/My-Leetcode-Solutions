# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        inorder = sorted(preorder)
        pre_map = {val: idx for idx, val in enumerate(inorder)}
        self.pre_idx = 0

        def build_bst(start, end):
            if start > end:
                return
            
            root_val = preorder[self.pre_idx]
            root = TreeNode(root_val)
            self.pre_idx += 1

            index = pre_map[root_val]

            root.left = build_bst(start, index - 1)
            root.right = build_bst(index + 1, end)

            return root
        
        return build_bst(0, len(inorder) - 1)
