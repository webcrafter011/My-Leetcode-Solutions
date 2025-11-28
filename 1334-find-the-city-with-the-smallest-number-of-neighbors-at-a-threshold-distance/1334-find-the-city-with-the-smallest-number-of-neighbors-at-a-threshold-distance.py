class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        cost = [[float('inf')] * n for _ in range(n)]

        for u, v, wt in edges:
            cost[u][v] = wt
            cost[v][u] = wt
        
        for u in range(n):
            cost[u][u] = 0
        

        for via in range(n):
            for i in range(n):
                for j in range(n):
                    if cost[i][via] != float('inf') and cost[via][j] != float('inf'):
                        cost[i][j] = min(
                            cost[i][j],
                            cost[i][via] + cost[via][j]
                        )
        
        counts = []
        for i in range(n):
            cnt = 0
            for j in range(n):
                if i != j and cost[i][j] <= distanceThreshold:
                    cnt += 1
            counts.append(cnt)
        

        city = -1
        minCount = float('inf')
        for i, cnt in enumerate(counts):
            if minCount >= cnt:
                minCount = cnt
                city = i
        
        return city