from flask import Flask

app = Flask(__name__)


@app.route('/')
def mainPage():
    return 'Flusk dockerized fork'


if __name__ == '__main__':
    app.run(debug = True,
            host = "0.0.0.0")
