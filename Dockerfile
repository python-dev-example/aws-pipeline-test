FROM python:3.7

MAINTAINER Vladyslav Maksymov (vmaksimov@ecisys.com)

COPY . /opt/octopus

EXPOSE 5000

WORKDIR /opt/octopus
ENV PYTHONPATH=/opt/octopus

RUN pip install -r requirements.txt

CMD python octopus/__init__.py
