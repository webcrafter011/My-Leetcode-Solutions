# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        idx_map = {val: idx for idx, val in enumerate(inorder)}
        self.pre_idx = 0

        def create_binary(start, end):
            if start > end:
                return 
            
            root = TreeNode(preorder[self.pre_idx])
            index = idx_map[preorder[self.pre_idx]]
            self.pre_idx += 1

            root.left = create_binary(start, index - 1)
            root.right = create_binary(index + 1, end)

            return root
        
        return create_binary(0, (len(inorder) - 1))