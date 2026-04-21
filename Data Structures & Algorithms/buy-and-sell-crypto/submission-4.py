class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        left = 0
        maximumProfit = prices[0] - prices[left]
        minimumBuy = prices[left]
        for i in range(1, len(prices)):
            if prices[i - 1] < minimumBuy:
                minimumBuy = prices[i - 1]
            if prices[i] - minimumBuy > maximumProfit:
                maximumProfit = prices[i] - minimumBuy
        return maximumProfit
            
            
        
        
        