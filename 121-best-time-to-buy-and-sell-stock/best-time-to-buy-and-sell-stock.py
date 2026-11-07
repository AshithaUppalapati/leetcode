class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_profit = inf 
        max_profit = 0
        for p in prices:
            min_profit = min(min_profit, p)
            max_profit = max(max_profit, p - min_profit)
        return max_profit