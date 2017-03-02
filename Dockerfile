FROM python:2.7-alpine

COPY requirements.txt /
COPY monitor.py /bin
COPY publish.py /bin

RUN pip install -r /requirements.txt


