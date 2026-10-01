class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        rank = 1
        n = len(arr)
        res = [-1] * n
        prev = None

        heap = []
        for i, num in enumerate(arr):
            heapq.heappush(heap, [num, i])

        while heap:
            el, i = heapq.heappop(heap)
            if prev and prev == el:
                res[i] = rank
                
            else:
                res[i] = rank
                
            if heap and heap[0][0] != el:
                rank += 1
            
            prev = el
        
        return res
