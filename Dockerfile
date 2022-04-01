# syntax=docker/dockerfile:1
FROM python:3.8-buster

WORKDIR /game

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY calcudungeon.py calcudungeon.py

CMD ["python3", "calcudungeon.py"]
