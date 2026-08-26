class Solution:

    def getAreaOfIsland(self, i, j, grid, currentArea):
        rightArea = 0
        leftArea = 0
        upArea = 0
        downArea = 0
        # Check to the right
        if j + 1 < len(grid[0]):
            if grid[i][j + 1] == 1:
                grid[i][j + 1] = 0
                rightArea = self.getAreaOfIsland(i, j + 1, grid, 1)
        # Check to the left
        if j - 1 >= 0:
            if grid[i][j - 1] == 1:
                grid[i][j - 1] = 0
                leftArea = self.getAreaOfIsland(i, j - 1, grid, 1)
        # Check above
        if i - 1 >= 0:
            if grid[i - 1][j] == 1:
                grid[i - 1][j] = 0
                upArea = self.getAreaOfIsland(i - 1, j, grid, 1)
        # Check below
        if i + 1 < len(grid):
            if grid[i + 1][j] == 1:
                grid[i + 1][j] = 0
                downArea = self.getAreaOfIsland(i + 1, j, grid, 1)
        return currentArea + rightArea + leftArea + downArea + upArea

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        boolean = True
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    currentArea = self.getAreaOfIsland(i, j, grid, 1)
                    if currentArea > maxArea:
                        maxArea = currentArea
        return maxArea

        