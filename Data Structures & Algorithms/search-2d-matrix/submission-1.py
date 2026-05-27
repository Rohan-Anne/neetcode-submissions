class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r = 0
        c = len(matrix[0]) - 1
        while 0 <= r < len(matrix) and 0 <= c < len(matrix[0]):
            print("Row index: " + str(r))
            print("Column index: " + str(c))
            if target == matrix[r][c]:
                return True
            elif target > matrix[r][c]:
                r += 1
            else:
                c -= 1
        return False

        