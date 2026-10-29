class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        counts = {}
        for c in tasks:
            counts[c] = counts.get(c, 0) + 1
        
        time = 0
        heap = [-cnt for cnt in counts.values()]
        heapq.heapify(heap)
        q = deque()

        while q or heap:
            time += 1

            if heap:
                cnt = 1 + heapq.heappop(heap)
                if cnt:
                    q.append((time + n, cnt))
            
            if q and q[0][0] <= time:
                heapq.heappush(heap, q.popleft()[1])

        return time


        
