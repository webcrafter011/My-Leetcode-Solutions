# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        idx_map = {val: idx for idx, val in enumerate(nums)}

        def build_tree(start, end):
            if start > end:
                return
            
            root_val = max(nums[start:end + 1])
            root = TreeNode(root_val)

            index = idx_map[root_val]

            root.left = build_tree(start, index - 1)
            root.right = build_tree(index + 1, end)

            return root
        
        return build_tree(0, len(nums) - 1)