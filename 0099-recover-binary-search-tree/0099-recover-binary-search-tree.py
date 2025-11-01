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
        pred = TreeNode(float('-inf'))
        first = middle = last = None

        curr = root
        while curr:
            if not curr.left:
                if pred.val > curr.val:
                    if not first:
                        first = pred
                        middle = curr
                    else:
                        last = curr
                pred = curr
                curr = curr.right
            else:
                prev = curr.left
                while prev.right and prev.right != curr:
                    prev = prev.right
                if not prev.right:
                    prev.right = curr
                    curr = curr.left
                else:
                    prev.right = None
                    if prev.val > curr.val:
                        if not first:
                            first = pred
                            middle = curr
                        else:
                            last = curr
                    pred = curr
                    curr = curr.right
        
        if first and last:
            first.val, last.val = last.val, first.val
        elif first and middle:
            first.val, middle.val = middle.val, first.val