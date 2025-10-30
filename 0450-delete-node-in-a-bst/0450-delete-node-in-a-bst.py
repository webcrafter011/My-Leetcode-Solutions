# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
        
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def get_rightmost(node):
            curr = node
            while curr.right:
                curr = curr.right
            return curr
            
        def helper(node):
            if not node.right:
                return node.left
            if not node.left:
                return node.right
            
            rightNode = node.right
            lefts_right_most = get_rightmost(node.left)
            lefts_right_most.right = rightNode
            return node.left

        if not root:
            return None
        if root.val == key:
            return helper(root)
        node = root
        while root:
            if root.val > key:
                if root.left and root.left.val == key:
                    root.left = helper(root.left)
                    break
                else:
                    root = root.left
            else:
                if root.right and root.right.val == key:
                    root.right = helper(root.right)
                    break
                else:
                    root = root.right

        return node
        
            