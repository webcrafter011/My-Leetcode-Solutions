# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        critical = []
        i = 0
        curr = head
        prev = None
        while curr:
            if prev and curr.next:
                if prev.val > curr.val < curr.next.val:
                    critical.append(i)
                elif prev.val < curr.val > curr.next.val:
                    critical.append(i)
            i += 1
            prev = curr
            curr = curr.next
        
        n = len(critical)
        if n <= 1:
            return [-1, -1]

        res = []
        mini = float('inf')
        for i in range(1, n):
            mini = min(mini, critical[i] - critical[i - 1])
        
        res.append(mini)

        maxi = critical[-1] - critical[0]
        res.append(maxi)
    
        return res