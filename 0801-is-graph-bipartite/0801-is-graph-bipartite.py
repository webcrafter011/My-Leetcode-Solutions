class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        colored = [-1] * n

        def dfs(i, grp):
            colored[i] = grp
            for nei in graph[i]:
                if colored[nei] == -1: # node is unvisited
                    if not dfs(nei, 1 - grp):
                        return False
                elif colored[nei] == grp:
                    return False
            return True
                
        
        for i in range(n):
            if colored[i] == -1:
                if not dfs(i, 0):
                    return False
        
        return True
