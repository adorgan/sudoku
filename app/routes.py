from app.__init__ import app
from flask import render_template, request, json
from app.helpers import algorithms


@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/verify', methods=['POST'])
def verify():
    vals = list(request.form.to_dict().values())
    if '' in vals:
        return 'Sorry, Try Again.'

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

    # if algorithms.validateSolution(grid):
    if algorithms.validateSolution(grid):
        return 'Correct!'
    else:
        return 'Sorry, Try Again.'


@app.route('/solve', methods=['POST'])
def solve():

    vals = list(request.form)[0][1:-1].split(',')

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
    solved = algorithms.getSolvedBoard(grid)
    return json.dumps(solved)
