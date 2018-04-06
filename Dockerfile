FROM python:3

ENV PYTHONUNBUFFERED 1
ENV EMAIL_ADDRESS="somemail@gmail.com"
ENV EMAILPWD="password"

RUN mkdir /home/CodeCollege
WORKDIR /home/CodeCollege

ADD requirements.txt .
RUN pip install -r requirements.txt
