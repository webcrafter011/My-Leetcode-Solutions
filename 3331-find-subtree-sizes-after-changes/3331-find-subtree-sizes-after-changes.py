class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        def dfs(i):
            
            ch = s[i]

            if ch in ancestors: prev = ancestors[ch]
            else: prev = None

            ancestors[ch] = i

            for node in graph[i]:
                dfs(node)
                ans[parent[node]] += ans[node]
            
            ancestors[ch] = prev
            if prev is None: return 
            
            parent[i] = prev
            return 


        ans = [1] * len(s)
        ancestors, graph = defaultdict(int), defaultdict(list)

        for node, par in enumerate(parent):
            graph[par].append(node)
        
        dfs(0)

        return ans
            

