# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        q = deque([(root, 0)])
        max_width = 0

        while q:
            _, first = q[0]
            _, last = q[-1]
            max_width = max(max_width, last - first + 1)

            for _ in range(len(q)):
                node, x = q.popleft()
                if node.left:
                    q.append((node.left, 2 * x))
                if node.right:
                    q.append((node.right, 2 * x + 1))
        
        return max_width