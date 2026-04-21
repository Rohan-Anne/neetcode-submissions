class Solution:
    def area(self, startX, finalX, height):
        return height * (finalX - startX)

    def maxArea(self, heights: List[int]) -> int:
        startIndex = 0
        finalIndex = len(heights) - 1
        maxArea = self.area(startIndex, finalIndex, min(heights[startIndex], heights[finalIndex]))
        while startIndex < finalIndex:
            currentArea = self.area(startIndex, finalIndex, min(heights[startIndex], heights[finalIndex]))
            if currentArea > maxArea:
                maxArea = currentArea
            if heights[finalIndex] > heights[startIndex]:
                startIndex += 1
            else:
                finalIndex -= 1
        return maxArea
        
        
            



            
        return maxArea
        
