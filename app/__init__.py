from flask import Flask, render_template, request
from app import algorithms
app = Flask(__name__)


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

    if algorithms.validateSolution(grid):
        return 'Correct!'
    else:
        return 'Sorry, Try Again.'


if __name__ == "__main__":
    app.run(host='0.0.0.0')
