class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0 
        sell  = 0
        max_profit = 0
        while sell < len(prices):
            if prices[sell] <= prices[buy]:
                buy = sell
            profit = prices[sell] - prices[buy]
            max_profit = max(profit, max_profit)
            sell += 1
        return max_profit