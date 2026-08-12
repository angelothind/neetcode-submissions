class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def isRowValid(row: List[str]) -> bool:
            rowMap = {}
            for number in row:
                if number != ".":
                    if (number in rowMap):
                        rowMap[number] = rowMap[number] + 1
                        return False
                    else:
                        rowMap[number] = 1
            return True

        def isColumnValid(column: int, board: List[List[str]]) -> bool:
            colMap = {}
            for number in range(0,9):
                currentValue = board[number][column]
                if currentValue != ".":
                    if (currentValue in colMap):
                        colMap[currentValue] = colMap[currentValue] + 1
                        return False
                    else:
                        colMap[currentValue] = 1
            return True

        def isSubBoxValid(board:List[List[str]], rowOrigin:int, colOrigin: int) -> bool:
            boxMap = {}
            currentRow = rowOrigin
            currentCol = colOrigin
            for i in range(0,3):
                currentCol = colOrigin

                for j in range(0,3):
                    currentVal = board[currentRow][currentCol]
                    if currentVal != ".":
                        if (currentVal in boxMap):
                            boxMap[currentVal] = boxMap[currentVal] + 1
                            return False
                        else:
                            boxMap[currentVal] = 1
                    currentCol += 1

                currentRow += 1
            return True
        
        rowOrigin = 0
        colOrigin = 0
        for i in range(0,9):
            if isRowValid(board[i]) == False:
                return False
            elif isColumnValid(i, board) == False:
                return False
                
        for rowOrigin in range(0, 9, 3):
            for colOrigin in range(0, 9, 3):
                if isSubBoxValid(board, rowOrigin, colOrigin) == False:
                    return False

        return True
                









        