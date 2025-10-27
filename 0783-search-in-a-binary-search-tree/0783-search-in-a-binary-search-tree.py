# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        find = None

        def dfs(root, val):
            nonlocal find
            if not root:
                return 
            if root.val == val:
                find = root
                return
            dfs(root.left, val)
            dfs(root.right, val)
        
        dfs(root, val)
        return find
            