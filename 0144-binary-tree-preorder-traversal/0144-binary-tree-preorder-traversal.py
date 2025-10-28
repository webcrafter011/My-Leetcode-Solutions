# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        preorder = []
        curr = root

        while curr:
            if not curr.left:
                preorder.append(curr.val)
                curr = curr.right
            else:
                prev = curr.left
                while prev.right and prev.right != curr:
                    prev = prev.right
                if prev.right:
                    prev.right = None
                    curr = curr.right
                else:
                    prev.right = curr
                    preorder.append(curr.val)
                    curr = curr.left
            
        return preorder