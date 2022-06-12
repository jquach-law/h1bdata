FROM docker.io/python:3.10-slim-buster
COPY . /
RUN pip install --disable-pip-version-check -r /requirements.txt
CMD gunicorn -b :$PORT app.main:app
