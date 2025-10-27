# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# from collections import deque

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:            
        graph = defaultdict(list)
        def build_graph(node, parent):
            if not node:
                return
            if parent:
                graph[node].append(parent)
                graph[parent].append(node)
            build_graph(node.left, node)
            build_graph(node.right, node)
        
        build_graph(root, None)
        
        res = []
        q = deque([(target, 0)])
        visited = set()
        visited.add(target)

        while q:
            node, dist = q.popleft()
            if dist == k:
                res.append(node.val)
            elif dist < k:
                for neighbour in graph[node]:
                    if neighbour not in visited:
                        visited.add(neighbour)
                        q.append((neighbour, dist + 1))
            
        return res