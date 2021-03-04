def checkRows(board):
    for i in range(0, 9):
        checkRow = [0] * 9
        for j in range(0, 9):
            checkRow[board[i][j] - 1] += 1
        if checkRow != [1] * 9:
            return False
    return True


def checkColums(board):
    for i in range(0, 9):
        checkCol = [0] * 9
        for j in range(0, 9):
            checkCol[board[j][i] - 1] += 1
        if checkCol != [1] * 9:
            return False
    return True


# def checkValidInput(board):
#     for row in board:
#         if len(row) != 9:
#             return False
#         for val in row:
#             if val < 1 or val > 9:
#                 return False
#     return True


def checkSubGrid(board):

    rowIndex = 0
    while rowIndex < 9:
        colIndex = 0
        while colIndex < 9:
            numList = [0] * 9
            for i in range(rowIndex, rowIndex+3):
                for j in range(colIndex, colIndex+3):
                    numList[board[i][j]-1] += 1
            if numList != [1] * 9:
                return False
            colIndex += 3
        rowIndex += 3
    return True


def validateSolution(board):
    if checkRows(board) \
            and checkColums(board) and checkSubGrid(board):

        return True
    else:
        return False
