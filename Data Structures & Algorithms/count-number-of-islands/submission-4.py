class Solution:
    def explore(self, i, j, grid):
        if i + 1 < len(grid):
            if grid[i + 1][j] == "1":
                grid[i + 1][j] = "0"
                self.explore(i + 1, j, grid)
        if i - 1 >= 0:
            if grid[i - 1][j] == "1":
                grid[i - 1][j] = "0"
                self.explore(i - 1, j, grid)
        if j + 1 < len(grid[i]):
            if grid[i][j + 1] == "1":
                grid[i][j + 1] = "0"
                self.explore(i, j + 1, grid)
        if j - 1 >= 0:
            if grid[i][j - 1] == "1":
                grid[i][j - 1] = "0"
                self.explore(i, j - 1, grid)
        return None
        




    def numIslands(self, grid: List[List[str]]) -> int:
        numIslands = 0
        i = 0
        while i < len(grid):
            j = 0
            while j < len(grid[i]):
                if grid[i][j] == "1":
                    numIslands += 1
                    grid[i][j] = "0"
                    self.explore(i, j, grid)
                j += 1
            i += 1
                
        return numIslands

        