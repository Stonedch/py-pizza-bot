FROM python:3.8.2-alpine

WORKDIR /usr/src/app

ADD Pipfile ./
ADD Pipfile.lock ./

RUN pip install --upgrade pip
RUN pip install pipenv

RUN pipenv install --system --deploy --ignore-pipfile

ADD ./src/ ./

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
