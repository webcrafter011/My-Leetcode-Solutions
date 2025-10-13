from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)

        heap = [(-count, num) for num, count in freq.items()]
        heapq.heapify(heap)

        res = []
        while k:
            count, num = heapq.heappop(heap)
            res.append(num)
            k -= 1
        
        return res