from flask import Flask, render_template
import platform
import psutil

app = Flask(__name__)

uname = platform.uname()

@app.route('/')
def mainPage():
    return render_template('index.html', system=psutil.cpu_count(logical=False))

@app.route('/cpu')
def cpuPage():
    return "CPU"

@app.route('/memory')
def memoryPage():
    return "MEMORY"

if __name__ == '__main__':
    app.run(debug = True, host = "0.0.0.0")
