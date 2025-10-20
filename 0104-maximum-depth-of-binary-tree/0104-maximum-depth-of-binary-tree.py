# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        height = 0
        q = deque([root])

        def bfs(node):
            nonlocal height
            while q:
                level_size = len(q)
                height += 1

                for _ in range(level_size):
                    node = q.popleft()

                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)

        bfs(root)
        return height