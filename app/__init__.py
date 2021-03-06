from flask import Flask
import app.routes


app = Flask(__name__)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
