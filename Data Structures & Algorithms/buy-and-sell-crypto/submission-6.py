class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # prices = [7,1,5,3,6,4]
        buy, sell = 0, 1
        maxP = 0

        while sell < len(prices):
            if prices[sell] > prices[buy]:
                profit = prices[sell] - prices[buy]
                if maxP < profit:
                    maxP = profit
            else:
                buy = sell
            
            # increment
            sell += 1
        
        return maxP
