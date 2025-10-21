# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque([(root, 0, 0)])
        nodes = []

        while q:
            node, x, y = q.popleft()
            if node:
                nodes.append((x, y, node.val))
                q.append((node.left, x - 1, y + 1))
                q.append((node.right, x + 1, y + 1))
        
        # sort the nodes array
        nodes.sort(key = lambda n: (n[0],  n[2]))

        res = defaultdict(list)
        for x, y, val in nodes:
            res[x].append(val)
        
        return [res[x] for x in sorted(res)]

