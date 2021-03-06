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


def checkValidInput(board):
    for row in board:
        if len(row) != 9:
            return False
        for val in row:
            if val < 1 or val > 9:
                return False
    return True


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
    if checkValidInput(board) and checkRows(board) \
            and checkColums(board) and checkSubGrid(board):

        return True
    else:
        return False


def checkSingleRow(board, row, num):
    checkList = [0] * 9
    for i in range(9):
        if board[row][i] != 0:
            checkList[board[row][i] - 1] += 1

    if checkList[num - 1] != 0:
        return False
    return True


def checkSingleCol(board, col, num):
    checkList = [0] * 9
    for i in range(9):
        if board[i][col] != 0:
            checkList[board[i][col] - 1] += 1

    if checkList[num - 1] != 0:
        return False
    return True


def checkSingleSubGrid(board, row, col, num):
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


def getSolvedBoard(board):
    temp = board
    solveBoard(temp)

    return temp


def solveBoard(board):
    emptySquare = findEmptySquare(board)
    if emptySquare is None:
        return True

    row = emptySquare[0]
    col = emptySquare[1]

    for i in range(1, 10):
        if valid(board, i, row, col):
            board[row][col] = i

            if solveBoard(board):
                return True

            board[row][col] = 0

    return False


def valid(board, num, row, col):
    if checkSingleRow(board, row, num) \
        and checkSingleCol(board, col, num) \
            and checkSingleSubGrid(board, row, col, num):
        return True

    return False


def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")


def findEmptySquare(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return [i, j]
    return None


# board = [[0, 7, 0, 9, 0, 2, 3, 0, 8], [0, 0, 0, 0, 6, 0, 0, 0, 0],
#          [0, 0, 0, 0, 5, 7, 1, 0, 6], [0, 0, 0, 0, 0, 0, 0, 0, 7],
#          [7, 6, 8, 4, 0, 0, 0, 0, 2], [0, 0, 0, 0, 0, 9, 0, 3, 0],
#          [1, 0, 0, 0, 7, 3, 2, 0, 0], [0, 8, 0, 0, 0, 1, 0, 4, 0],
#          [0, 0, 0, 0, 0, 0, 0, 6, 0]]
# print_board(board)
# solve(board)
# print("___________________")
# print_board(board)
