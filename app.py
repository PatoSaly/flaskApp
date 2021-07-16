from flask import Flask, render_template
import platform
import psutil

from datetime import datetime


app = Flask(__name__)

def conversion(num):
    step = 1000.0
    for size in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < step:
            return "%3.1f %s" % (num, size)
        num /= step


@app.route('/')
def mainPage():
    uname = platform.uname()
    svmem = psutil.virtual_memory()
    cpufreq = psutil.cpu_freq()

    return render_template('index.html',
                            system=uname.system,
                            processor=uname.processor,
                            cores=psutil.cpu_count(logical=True),
                            totalRam=conversion(svmem.total),
                            maxFreq= str(cpufreq.max) + 'Mhz',
                            currFreq= str(cpufreq.current) + 'Mhz',
                            avRam= conversion(svmem.available),
                            usedRam = conversion(svmem.used),
                            percRam = str(svmem.percent) + '%'
                            )

if __name__ == '__main__':
    app.run(debug = True, host = "0.0.0.0")
