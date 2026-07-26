class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        row = set()
        column = set()
        rowcol = set()
        #row
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == ".":
                    continue
                if board[i][j] in row:
                    return False
                else:
                    row.add(board[i][j])
            row.clear()
            

        #column
        for i in range(len(board)):
            for j in range(len(board)):
                if board[j][i] == ".":
                    continue
                if board[j][i] in column:
                    return False
                else:
                    column.add(board[j][i])
            column.clear()

        #rowcolumn
        for box_row in range(0, 9, 3):      # 0, 3, 6 → which box, row-wise
            for box_col in range(0, 9, 3):  # 0, 3, 6 → which box, column-wise
                for i in range(3):
                    for j in range(3):
                        row_index = box_row + i
                        col_index = box_col + j
                        if board[row_index][col_index] == ".":
                            continue
                        if board[row_index][col_index] in rowcol:
                           return False
                        else:
                           rowcol.add(board[row_index][col_index])
                rowcol.clear()


        return True