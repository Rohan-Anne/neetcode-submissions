class Solution:
    # Helper function to convert indices between 1D and 2D for ease of binary search
    def return2DIndex(self, index: int, n: int) -> List[int]:
        firstIndex = index // n
        secondIndex = -1
        if index >= n:
            secondIndex = index % n
        else:
            secondIndex = index
        return [firstIndex, secondIndex]
    # Actual binary search algorithm

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        l = 0
        r = len(matrix) * len(matrix[0]) - 1
        while l <= r:
            if l == r:
                l1, l2 = self.return2DIndex(l, n)
                if matrix[l1][l2] == target:
                    return True
                else:
                    return False
            else:
                currentIndex = int((l + r) / 2)
                m1, m2 = self.return2DIndex(currentIndex, n)
                if matrix[m1][m2] == target:
                    return True
                elif matrix[m1][m2] < target:
                    l = currentIndex + 1
                else:
                    r = currentIndex
        return False
        