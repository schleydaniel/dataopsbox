# syntax=docker/dockerfile:1

FROM python:3.11-slim-buster

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
RUN apt-get clean \
    && apt-get -y update && apt-get install -y vim && apt-get install -y bash-completion \
    && apt-get -y install python3-dev \
    && apt-get -y install build-essential
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Upgrade PIP
RUN pip install --upgrade pip

# Install dependencies:
COPY . /srv/flask_app/
WORKDIR /srv/flask_app

RUN pip install -r requirements.txt --src /usr/local/src

#EXPOSE 5051

#COPY /templates /app/templates
#COPY requirements.txt /app/
#COPY app.py /app/
#WORKDIR /app
#RUN pip install -r requirements.txt
CMD ["gunicorn"  , "-b", "0.0.0.0:5051", "--workers", "2", "--threads", "100", "app:app"]
