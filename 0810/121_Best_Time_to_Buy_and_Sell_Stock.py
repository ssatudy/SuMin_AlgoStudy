class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_val = prices[-1]
        profit = 0
        for price in prices[::-1]:
            if price > max_val:
                max_val = price
            if max_val-price > profit:
                profit = max_val-price
        
        return(profit)