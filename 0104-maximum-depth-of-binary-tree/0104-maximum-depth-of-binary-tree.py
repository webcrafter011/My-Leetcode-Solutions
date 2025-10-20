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
        res = []
        q = deque([root])

        def bfs(node):
            while q:
                level_nodes = []
                level_size = len(q)

                for _ in range(level_size):
                    node = q.popleft()
                    level_nodes.append(node.val)

                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)

                res.append(level_nodes)

        bfs(root)
        return len(res)