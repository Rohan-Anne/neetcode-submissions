class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        currentRow = len(matrix) - 1
        currentColumn = 0
        current = 0
        while currentRow >= 0 and currentColumn < len(matrix[0]):
            current = matrix[currentRow][currentColumn]
            if current == target:
                return True
            elif current < target:
                currentColumn += 1
            else:
                currentRow -= 1 
        
        return current == target 
        

        