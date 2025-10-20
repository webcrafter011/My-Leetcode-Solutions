# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # result = []

        # def dfs(node):
        #     if not node:
        #         return
            
        #     dfs(node.left)
        #     dfs(node.right)
        #     result.append(node.val)
        
        # dfs(root)
        # return result
        if not root:
            return []
        
        st1 = [root]
        st2 = []
        
        while st1:
            node = st1.pop()
            st2.append(node)
            
            if node.left:
                st1.append(node.left)
            if node.right:
                st1.append(node.right)
        
        return [node.val for node in st2][::-1]

