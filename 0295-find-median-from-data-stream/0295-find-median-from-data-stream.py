import heapq

class MedianFinder:

    def __init__(self):
        # we will have two heaps
        # 1. max-heap to keep track of left half values
        # we need to push negative values in left half
        self.left = []

        # 2. min-heap to kep track of right half values
        # no need to push negative values in the right half 
        self.right = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.left, -num)
        if self.left and self.right and -self.left[0] > self.right[0]:
            val = -heapq.heappop(self.left)
            heapq.heappush(self.right, val)

        # if uneven size (~)
        if len(self.left) >  1 + len(self.right):
            val = -heapq.heappop(self.left)
            heapq.heappush(self.right, val)
        if len(self.right) > 1 + len(self.left):
            val = heapq.heappop(self.right)
            heapq.heappush(self.left, -val)
        

    def findMedian(self) -> float:
        if len(self.left) > len(self.right):
            return -self.left[0]
        if len(self.right) > len(self.left):
            return self.right[0]
        
        return (-self.left[0] + self.right[0]) / 2