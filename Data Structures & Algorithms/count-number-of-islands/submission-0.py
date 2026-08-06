class Solution:

    def exploreIsland(self, start, coordinates, removals):
        i = start[0]
        j = start[1]

        if (i + 1, j) not in coordinates and (i - 1, j) not in coordinates and (i, j + 1) not in coordinates and (i, j - 1) not in coordinates:
            removals.add(start)
            return removals
        rightRemovals = removals
        leftRemovals = removals
        upRemovals = removals
        downRemovals = removals
        if (i + 1, j) in coordinates and (i + 1, j) not in removals:
            removals.add((i + 1, j))
            rightRemovals = self.exploreIsland((i + 1, j), coordinates, removals)
        if (i - 1, j) in coordinates and (i - 1, j) not in removals:
            removals.add((i - 1, j))
            leftRemovals = self.exploreIsland((i - 1, j), coordinates, removals)
        if (i, j + 1) in coordinates and (i, j + 1) not in removals:
            removals.add((i, j + 1))
            downRemovals = self.exploreIsland((i, j + 1), coordinates, removals)
        if (i, j - 1) in coordinates and (i, j - 1) not in removals:
            removals.add((i, j - 1))
            upRemovals = self.exploreIsland((i, j - 1), coordinates, removals)
        
        combinedRemovals = rightRemovals.union(leftRemovals, downRemovals, upRemovals)
        return combinedRemovals
        



    def numIslands(self, grid: List[List[str]]) -> int:
        # Get coordinates of all land elements
        coordinates = set()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    coordinates.add((i, j))
        print(coordinates)
        numIslands = 0
        while len(coordinates) > 0:
            start = next(iter(coordinates))
            print(start)
            removals = set()
            removals = self.exploreIsland(start, coordinates, removals)
            coordinates = coordinates - removals
            numIslands += 1
        
        return numIslands
            
            

        

        