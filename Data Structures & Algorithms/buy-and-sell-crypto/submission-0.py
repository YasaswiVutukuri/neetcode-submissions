class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1  # l = buy day, r = sell day
        max_profit = 0
        
        while r < len(prices):
            # Is the transaction profitable?
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                max_profit = max(max_profit, profit)
            else:
                # Found a lower buy price! Slide left pointer to r
                l = r
            
            # Always move right pointer to explore next sell day
            r += 1
            
        return max_profit