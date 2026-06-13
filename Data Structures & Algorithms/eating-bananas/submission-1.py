class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        numBananas = 0
        maxBananas = -1
        rates = []
        # Find total number of bananas and biggest pile
        for i in range(len(piles)):
            numBananas += piles[i]
            if piles[i] > maxBananas:
                maxBananas = piles[i]
    
        l = 0
        r = maxBananas - 1
        
        while l < r:
            m = int((l + r) / 2)
            rate = m + 1
            hours = 0
            # Calculated hours needed
            for i in range(len(piles)):
                if piles[i] % rate == 0:
                    hours += piles[i] / rate
                else:
                    hours += int(piles[i] / rate) + 1

            # TODO: FIGURE OUT HOW TO MOVE THROUGH ITERATION
            if hours <= h: # correct eating rate, this can be our new minimum
                r = m
            elif hours > h: # need a bigger eating rate
                l = m + 1
        
        return l + 1
            
        

            

            
                

            
        
        
        

        
        
        

        

        


        