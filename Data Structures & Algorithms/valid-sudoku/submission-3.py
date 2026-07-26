class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:


        row = defaultdict(set)
        column = defaultdict(set)
        rowcol = defaultdict(set)
        #row
        for i in range(9):
            for j in range(9):
                value = board[i][j]

                if value == '.':
                    continue
                
                box = (i//3,j//3)

                if (value in row[i] or value in column[j] or value in rowcol[box]):
                    return False

                row[i].add(value)     
                column[j].add(value) 
                rowcol[box].add(value)  

        return True      