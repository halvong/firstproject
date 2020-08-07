FROM python:3.8.2
LABEL maintainer="halvong@yahoo.com"

#avoids buffered
ENV PYTHONBUFFERED 1
ENV DJANGO_SETTINGS_MODULE firstproject.settings

COPY ./requirements.txt /requirements.txt
RUN pip install --upgrade pip
RUN pip install -r /requirements.txt

RUN mkdir /usr/src/app
WORKDIR /usr/src/app
COPY . /usr/src/app

#creates user and home directory in linux image
RUN useradd -ms /bin/bash tom
