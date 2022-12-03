class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_num = float("inf")
        for i in range(len(prices)):
            max_profit_by_selling_now = prices[i] - min_num
            max_profit = max(max_profit, max_profit_by_selling_now)
            min_num = min(min_num, prices[i])
        return max_profit
