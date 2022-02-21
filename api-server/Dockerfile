FROM docker.io/python:3.10-slim-buster
COPY ./requirements.txt /requirements.txt
RUN pip install --disable-pip-version-check -r /requirements.txt
COPY ./app /app
COPY ./.env /.env
COPY ./root.crt /root.crt
CMD gunicorn -b :$PORT app.main:app
