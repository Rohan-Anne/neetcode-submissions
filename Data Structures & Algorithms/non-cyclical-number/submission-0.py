class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while True:
            numString = str(n)
            numSum = 0
            for char in numString:
                numSum += int(char) * int(char)
            if numSum in seen:
                return False
            elif numSum == 1:
                return True
            seen.add(numSum)
            n = numSum
        
            
            

        