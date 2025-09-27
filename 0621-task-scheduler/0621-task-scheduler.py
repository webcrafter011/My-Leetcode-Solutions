import heapq
from collections import deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        heap = [-cnt for cnt in count.values()]
        heapq.heapify(heap)
        dq = deque()

        time = 0
        while heap or dq:
            if heap:
                cnt = 1 + heapq.heappop(heap)
                if cnt:
                    dq.append([cnt, time + n])
            if dq and dq[0][1] == time:
                heapq.heappush(heap, dq.popleft()[0])
            time += 1
        
        return time
                
            