class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # prices = [7,1,5,3,6,4]
        minBuy = prices[0]
        maxP = 0

        for i, price in enumerate(prices):
            if price > minBuy:
                profit = price - minBuy
                if maxP < profit:
                    maxP = profit
            else:
                minBuy = price
        
        return maxP
