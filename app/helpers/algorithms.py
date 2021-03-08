# VERIFICATION #

def checkRows(board):
    # check all board rows for duplicate numbers
    for i in range(0, 9):
        checkRow = [0] * 9
        for j in range(0, 9):
            checkRow[board[i][j] - 1] += 1
        if checkRow != [1] * 9:
            return False
    return True


def checkColums(board):
    # check all columns for duplicate numbers
    for i in range(0, 9):
        checkCol = [0] * 9
        for j in range(0, 9):
            checkCol[board[j][i] - 1] += 1
        if checkCol != [1] * 9:
            return False
    return True


def checkValidInput(board):
    # check for valid inputs
    for row in board:
        if len(row) != 9:
            return False
        for val in row:
            if val < 1 or val > 9:
                return False
    return True


def checkSubGrid(board):
    # check each subgrid for duplicate numbers
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
    # check if user answerse are correct
    if checkValidInput(board) and checkRows(board) \
            and checkColums(board) and checkSubGrid(board):
        return True
    else:
        return False

# --------------------------------------------------------------#
# SOLVING #
# modeled after: https://www.youtube.com/watch?v=lK4N8E6uNr4


def findEmptySquare(board):
    # find square to fill in
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return [i, j]
    return None


def checkSingleRow(board, row, num):
    # check current row for duplicate numbers
    checkList = [0] * 9
    for i in range(9):
        if board[row][i] != 0:
            checkList[board[row][i] - 1] += 1

    if checkList[num - 1] != 0:
        return False
    return True


def checkSingleCol(board, col, num):
    # check current column for duplicate numbers
    checkList = [0] * 9
    for i in range(9):
        if board[i][col] != 0:
            checkList[board[i][col] - 1] += 1

    if checkList[num - 1] != 0:
        return False
    return True


def checkSingleSubGrid(board, row, col, num):
    # check current subgrid for duplicate numbers
    checkList = [0] * 9
    subGridX = row - (row % 3)
    subGridY = col - (col % 3)
    for i in range(subGridX, subGridX + 3):
        for j in range(subGridY, subGridY + 3):
            if board[i][j] != 0:
                checkList[board[i][j] - 1] += 1
    if checkList[num - 1] != 0:
        return False
    return True


def valid(board, num, row, col):
    # see if all checks pass for current square/number
    if checkSingleRow(board, row, num) \
        and checkSingleCol(board, col, num) \
            and checkSingleSubGrid(board, row, col, num):
        return True

    return False


def solveBoard(board):
    # first find an empty square
    emptySquare = findEmptySquare(board)
    if emptySquare is None:
        # no empty squares means board is complete
        return True

    # assign row,col of empty square
    row = emptySquare[0]
    col = emptySquare[1]

    for i in range(1, 10):
        # try each possible number choice for an empty square
        if valid(board, i, row, col):
            # if the number is not a duplicate, assign to that square
            board[row][col] = i

            if solveBoard(board):
                # recursively solve the rest of the board
                return True

            board[row][col] = 0
    # no number works, so must backtrack
    return False
