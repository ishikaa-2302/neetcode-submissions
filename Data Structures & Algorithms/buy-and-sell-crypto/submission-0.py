class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #if profit<=0, return 0
        #if profit>0, return proft[i]-profit[j]
        buy = 0
        sell = 0
        max_profit = 0
        for i in range(len(prices)):
            if prices[sell] < prices[buy]:
                buy = sell
            else:
                max_profit = max(max_profit, prices[sell] - prices[buy])
            sell+=1
        return max_profit