class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_profilt = 0
        min_price = prices[0]

        for i in range(1,len(prices)):

            if prices[i] < min_price:
                min_price = prices[i]
            elif prices[i] > min_price:
                current_profit = prices[i] - min_price
                max_profilt = max(current_profit,max_profilt)
            else:
                continue
        
        return max_profilt
        