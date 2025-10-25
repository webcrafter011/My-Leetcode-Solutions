# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
6
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def get_nodes(node):
            if not node:
                return 0

            lh = left_height(node)
            rh = right_height(node)

            if lh == rh:
                return (1 << lh) - 1
            
            return 1 + get_nodes(node.right) + get_nodes(node.left)
        
        def left_height(node):
            height = 0
            curr = node
            while curr:
                height += 1
                curr = curr.left
            return height
        
        def right_height(node):
            height = 0
            curr = node
            while curr:
                curr = curr.right
                height += 1
            return height
        
        return get_nodes(root)