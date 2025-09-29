import heapq

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        count = Counter(hand)
        for x in sorted(count):
            while count[x] > 0:
                need = count[x]
                for i in range(groupSize):
                    if count[x + i] < need:
                        return False
                    count[x + i] -= need
        return True
