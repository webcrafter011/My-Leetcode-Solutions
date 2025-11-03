# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.summation = 0

        while root:
            if not root.left:
                if low <= root.val <= high:
                    self.summation += root.val
                root = root.right
            else:
                prev = root.left
                while prev.right and prev.right != root:
                    prev = prev.right
                if not prev.right:
                    prev.right = root
                    root = root.left
                elif prev.right:
                    prev.right = None
                    if low <= root.val <= high:
                        self.summation += root.val
                    root = root.right
                 
    
        return self.summation