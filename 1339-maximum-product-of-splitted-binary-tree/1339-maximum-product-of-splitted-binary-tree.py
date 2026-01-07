# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD = 10**9 + 7
        maxi = 0

        def count_total(node):
            total = node.val
            if node.left:
                total += count_total(node.left)
            if node.right:
                total += count_total(node.right)
            
            return total

        total_sum = count_total(root)

        # post order: left -> right -> root
        def dfs(node):
            if not node:
                return 0

            nonlocal maxi

            left = dfs(node.left)
            right = dfs(node.right)
            subtree_sum = left + right + node.val
            
            first = total_sum - subtree_sum
            curr_prod = (first * subtree_sum)
            maxi = max(maxi, curr_prod)

            return subtree_sum
            
        dfs(root)
    
        return maxi % MOD