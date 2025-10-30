# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return None
        min_heap = []

        def dfs(node):
            if not node:
                return
            min_heap.append(node.val)
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        
        heapq.heapify(min_heap)
        for i in range(k - 1):
            heapq.heappop(min_heap)
        
        return min_heap[0]
        