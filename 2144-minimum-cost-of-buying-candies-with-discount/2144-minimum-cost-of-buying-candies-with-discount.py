class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)
        c1 = 0
        c2 = 1
        # f = 2
        n = len(cost)
        tcost = 0

        while c1 < n or c2 < n:
            curr_cost = 0

            if c1 < n:
                curr_cost += cost[c1]
                print(f'c1 = {cost[c1]}')
            if c2 < n:
                curr_cost += cost[c2]
                print(f'c2 = {cost[c2]}')
            
            tcost += curr_cost
            c1 += 3
            c2 += 3
    
        return tcost