class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = min(heights[0], heights[-1]) * (len(heights) - 1)
        start = 0
        end = len(heights) - 1
        while (start < end):
            if heights[start] <= heights[end]:
                start += 1
            else:
                end -= 1

            if min(heights[start], heights[end]) * (end - start) > maxArea:
                maxArea = min(heights[start], heights[end]) * (end - start)
        
        return maxArea
                    

                




        