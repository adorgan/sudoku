import os

from flask import Flask, render_template, request


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


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello

    @app.route('/')
    def hello():
        return render_template('index.html')

    @app.route('/verify', methods=['POST'])
    def verify():
        vals = list(request.form.to_dict().values())
        if '' in vals:
            return 'Sorry, Try Again.'

        print(len(vals))
        grid = []
        row = []
        for i in range(len(vals)):
            if i != 0 and i % 9 == 0:
                grid.append(row)
                row = []
                row.append(int(vals[i]))
            else:
                row.append(int(vals[i]))
        grid.append(row)

        if validateSolution(grid):
            return 'Correct!'
        else:
            return 'Sorry, Try Again.'

    return app
