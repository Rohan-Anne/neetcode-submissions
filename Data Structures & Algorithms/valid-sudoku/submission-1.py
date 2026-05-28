class Solution:
    

    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = [set(), set(), set(), set(), set(), set(), set(), set(), set()]
        columns = [set(), set(), set(), set(), set(), set(), set(), set(), set()]
        grids = [set(), set(), set(), set(), set(), set(), set(), set(), set()]

     
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == ".":
                    continue

                gridIndex = 3 * int(i / (len(board) / 3)) + int(j / (len(board) / 3))
                if board[i][j] in rows[i] or board[i][j] in columns[j] or board[i][j] in grids[gridIndex]:
                    print(rows[0])
                    print("Failed on row " + str(i) + " and column " + str(j) + " and grid " + str(gridIndex) + " with value " + board[i][j])
                    return False
                else:
                    rows[i].add(board[i][j])
                    columns[j].add(board[i][j])
                    grids[gridIndex].add(board[i][j])

                    print("Row " + str(i) + " now has"  + str(list(rows[i])))
                    print("Column " + str(j) + " now has " + str(list(columns[j])))
                    print("Grid " + str(gridIndex) + " now has " + str(list(grids[gridIndex])))
        
        return True 
                
                    
                

        