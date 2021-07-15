from flask import Flask, render_template
import platform
import psutil

from datetime import datetime


app = Flask(__name__)
cislo = 10


@app.route('/')
def mainPage():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    return render_template('index.html', time=current_time)

@app.route('/cpu')
def cpuPage():
    return "CPU"

@app.route('/memory')
def memoryPage():
    return "MEMORY"

if __name__ == '__main__':
    app.run(debug = True, host = "0.0.0.0")
