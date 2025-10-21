# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []
        q = deque([root])
        left_to_right = True

        while q:
            level_nodes = []
            
            for _ in range(len(q)):
                node = q.popleft()
                level_nodes.append(node.val)
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            if left_to_right:
                result.append(level_nodes)
                left_to_right = False
            else:
                result.append(level_nodes[::-1])
                left_to_right = True
        
        return result