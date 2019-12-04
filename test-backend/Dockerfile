FROM ubuntu

ENV LANG C.UTF-8

COPY person.py person.py

RUN apt-get update
RUN apt-get -y install python3.6
RUN apt -y install python3-pip

RUN pip3 install flask
RUN pip3 install mysql-connector

EXPOSE 5000

ENTRYPOINT python3 person.py
