FROM python:3

ENV PYTHONUNBUFFERED 1
ENV EMAIL_ADDRESS somemail@gmail.com
ENV EMAIL_PWD password

RUN mkdir -p /home/CodeCollege/code_college/tests_coverage
WORKDIR /home/CodeCollege/code_college

ADD requirements.txt ..
RUN pip install -r ../requirements.txt
