class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        maximumWeight = None
        sumWeights = 0
        for i in range(len(weights)):
            if maximumWeight is None or weights[i] > maximumWeight:
                maximumWeight = weights[i]
            sumWeights += weights[i]
        left = maximumWeight
        right = sumWeights
        while left < right:
            m = int((left + right) / 2)
            print(left)
            print(right)
            print(m)
            currentDays = 1
            capacity = m
            j = 0
            while j < len(weights):
                if weights[j] <= capacity:
                    capacity = capacity - weights[j]
                    j += 1
                else:
                    capacity = m
                    currentDays += 1
            if currentDays <= days:
                right = m
            else:
                left = m + 1
        return left
            

                
            # Calculate days needed


        