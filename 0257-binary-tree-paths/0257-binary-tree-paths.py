# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def is_leaf(node):
            return not node.left and not node.right

        res = []
        def recurse(node, path):
            if is_leaf(node):
                path += str(node.val)
                res.append(path)
                return 
            path += str(node.val) + '->'
            if node.left:
                recurse(node.left, path)
            if node.right:
                recurse(node.right, path)
        
        recurse(root, '')
        return res
            