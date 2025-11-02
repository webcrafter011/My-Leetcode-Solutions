# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.result = None
        self.rank = 0

        # def inorder(node):
        #     if not node:
        #         return
        #     if self.result is not None:
        #         return
            
        #     inorder(node.left)

        #     self.rank += 1
        #     if self.result is None and self.rank == k:
        #         self.result = node.val
        #         return
        
        #     inorder(node.right)
        
        # inorder(root)
        # return self.result
        
        # trial with morris traversal 
        node = root

        while node:
            if not node.left:
                self.rank += 1
                if self.rank == k:
                    self.result = node.val
                    break
                node = node.right
            else:
                prev = node.left
                while prev.right and prev.right != node:
                    prev = prev.right
                if not prev.right:
                    prev.right = node
                    node = node.left
                elif prev.right:
                    prev.right = None
                    self.rank += 1
                    if self.rank == k:
                        self.result = node.val
                        break
                    node = node.right
        
        return self.result