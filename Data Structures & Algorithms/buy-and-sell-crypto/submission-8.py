class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        start = 0
        end = 0
        maxProfit = prices[end] - prices[start]
        for i in range(1, len(prices)):
            if prices[i] < prices[start]:
                if prices[end] - prices[start] > maxProfit:
                    maxProfit = prices[end] - prices[start]
                start = i
                end = i

            if prices[i] - prices[start] > maxProfit:
                end = i
                maxProfit = prices[end] - prices[start]
            
            print("Current index causing update: " + str(i))
            print("Start index: " + str(start))
            print("End index: " + str(end))            
            print("Max profit: " + str(maxProfit))

        return maxProfit

            


        