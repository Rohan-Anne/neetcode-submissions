class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        freshFruits = set()
        rottenFruits = set()
        minutes = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                    rottenFruits.add((i, j))
                if grid[i][j] == 1:
                    freshFruits.add((i, j))
        
        while len(freshFruits) > 0:
            currentRotten = rottenFruits.copy()
            for fruit in currentRotten:
                # Check adjacent positions in fresh fruits and update sets
                if (fruit[0] - 1, fruit[1]) in freshFruits:
                    freshFruits.remove((fruit[0] - 1, fruit[1]))
                    rottenFruits.add((fruit[0] - 1, fruit[1]))
                if (fruit[0] + 1, fruit[1]) in freshFruits:
                    freshFruits.remove((fruit[0] + 1, fruit[1]))
                    rottenFruits.add((fruit[0] + 1, fruit[1]))
                if (fruit[0], fruit[1] - 1) in freshFruits:
                    freshFruits.remove((fruit[0], fruit[1] - 1))
                    rottenFruits.add((fruit[0], fruit[1] - 1))
                if (fruit[0], fruit[1] + 1) in freshFruits:
                    freshFruits.remove((fruit[0], fruit[1] + 1))
                    rottenFruits.add((fruit[0], fruit[1] + 1))
            if currentRotten == rottenFruits:
                return -1
            minutes += 1
        return minutes


                