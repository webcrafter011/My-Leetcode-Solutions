class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        smallest = prices[0]
        max_profit = 0

        for i in range(len(prices)):
            if smallest < prices[i]:
                max_profit = max(max_profit, prices[i] - smallest)
            else:
                smallest = prices[i]
        
        return max_profit 