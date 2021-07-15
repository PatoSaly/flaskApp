# Dockerfile -> Image -> Container

FROM python:3.8

ADD app.py .

RUN pip install Flask

CMD ["python", "./app.py"]


