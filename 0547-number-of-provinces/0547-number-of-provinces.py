from collections import defaultdict

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        adj = defaultdict(list)

        n = len(isConnected)
        for i in range(n):
            for j in range(n):
                if isConnected[i][j]:
                    adj[i].append(j)
                    adj[j].append(i)
        
        vis = set()
        count = 0
        
        def dfs(node):
            vis.add(node)
            for nei in adj[node]:
                if nei not in vis:
                    dfs(nei)
        
        for i in range(n):
            if i not in vis:
                dfs(i)
                count += 1
        
        return count