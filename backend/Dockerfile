FROM python:3.7

RUN pip3 install flask
RUN pip3 install mysql-connector
COPY ./person.py ./person.py

ENTRYPOINT python3 ./person.py
