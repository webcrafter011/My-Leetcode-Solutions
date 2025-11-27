class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 10**9 + 7

        adj = defaultdict(list)
        for u, v, time in roads:
            adj[u].append((v, time))
            adj[v].append((u, time))
        
        ways = [0] * n
        dist = [float('inf')] * n
        ways[0] = 1
        dist[0] = 0

        pq = [(0, 0)] # dist, node

        while pq:
            dst, node = heapq.heappop(pq)

            for nei, wt in adj[node]:
                new_wt = wt + dst
                if new_wt < dist[nei]:
                    dist[nei] = new_wt
                    ways[nei] = ways[node]
                    heapq.heappush(pq, (dist[nei], nei))
                elif new_wt == dist[nei]:
                    ways[nei] += ways[node] % MOD
        
        return ways[n - 1] % MOD
