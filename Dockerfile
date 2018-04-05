FROM python:3

ENV PYTHONUNBUFFERED 1

RUN mkdir /home/CodeCollege
WORKDIR /home/CodeCollege

ADD requirements.txt .
RUN pip install -r requirements.txt
