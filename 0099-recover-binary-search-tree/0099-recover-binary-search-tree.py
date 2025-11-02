# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.first = self.middle = self.last = None
        self.prev = TreeNode(float('-inf'))

        def inorder(node):
            if not node:
                return
            
            inorder(node.left)

            # current node operation
            if self.prev.val > node.val:
                if not self.first:
                    self.first = self.prev
                    self.middle = node
                else:
                    self.last = node
            
            self.prev = node

            inorder(node.right)
        
        inorder(root)
        

        if self.first and self.last:
            self.first.val, self.last.val = self.last.val, self.first.val
        elif self.first and self.middle:
            self.first.val, self.middle.val = self.middle.val, self.first.val