# Dockerfile -> Image -> Container

FROM python:3.8

WORKDIR /app

ADD app.py .

COPY templates /app/templates
COPY static /app/static

RUN pip install Flask psutil

CMD ["python", "./app.py"]


#prikazy potrebne na spustenie programu
#aplikacia bezi na localhoste s portom 5000

#build
#docker build -t hardwareinfo .

#spustenie
#docker run -d -p 5000:5000 --name work-app hardwareinfo

#ukoncenie
#docker stop work-app

#odstranenie; potrebne pri opakovanom spusteni
#docker rm work-app
