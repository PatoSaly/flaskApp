# Dockerfile -> Image -> Container

FROM python:3.8

WORKDIR /app

ADD app.py .

COPY templates /app/templates

RUN pip install Flask psutil

CMD ["python", "./app.py"]


#prikazy potrebne na spustenie programu

#docker build -t hardwareinfo .
#docker run -p 5000:5000 hardwareinfo

#aplikacia bezi na localhoste s portom 5000
