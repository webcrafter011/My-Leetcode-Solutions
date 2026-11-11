
class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:

        # Only individual items
        a = cost1 * need1 + cost2 * need2

        # Only combined items
        b = costBoth * max(need1, need2)

        # Mixed purchasing
        common = min(need1, need2)

        c = (
            costBoth * common
            + cost1 * (need1 - common)
            + cost2 * (need2 - common)
        )

        return min(a, b, c)
