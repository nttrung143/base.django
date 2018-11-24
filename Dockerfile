FROM python:slim-jessie
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD Pipfile /code/
ADD Pipfile.lock /code/
RUN pip install pipenv
RUN pipenv install --system
ADD . /code/