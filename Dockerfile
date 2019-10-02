FROM python:3.7

MAINTAINER Vladyslav Maksymov (vmaksimov@ecisys.com)

COPY . /opt/app

EXPOSE 5000

WORKDIR /opt/app
ENV PYTHONPATH=/opt/app

RUN pip install -r requirements.txt

CMD python app/__init__.py
