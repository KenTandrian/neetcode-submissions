class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # prices = [10,1,5,6,7,1]
        max_profit = 0

        for i in range(0, len(prices)):
            for j in range(i, len(prices)):
                profit = prices[j] - prices[i]
                if profit > max_profit:
                    max_profit = profit
        
        return max_profit
