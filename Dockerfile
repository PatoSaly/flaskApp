# Dockerfile -> Image -> Container

FROM python:3.8

ADD app.py .

RUN pip install Flask

CMD ["python", "./app.py"]

#prikazy potrebne na spustenie programu
#docker build -t hardwareinfo .

#docker run -p 5000:5000 hardwareinfo
