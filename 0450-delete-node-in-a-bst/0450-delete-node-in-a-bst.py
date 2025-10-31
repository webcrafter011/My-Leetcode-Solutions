# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def helper(node):
            if not node.left:
                return node.right
            if not node.right:
                return node.left
            
            rightNode = node.right
            lefts_rightmost = get_rightmost(node.left)
            lefts_rightmost.right = rightNode
            return node.left
        
        def get_rightmost(node):
            while node.right:
                node = node.right
            return node


        if not root:
            return None 
        if root.val == key:
            return helper(root)
        
        dummy = root
        
        while root:
            if root.val > key:
                if root.left and root.left.val == key:
                     root.left = helper(root.left)
                     break
                root = root.left
            elif root.val < key:
                if root.right and root.right.val == key:
                    root.right = helper(root.right)
                    break
                root = root.right
        
        return dummy