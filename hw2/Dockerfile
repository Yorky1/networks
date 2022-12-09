# syntax=docker/dockerfile:1

FROM python:latest

RUN mkdir script
WORKDIR /script

RUN apt-get update && apt-get install -y iputils-ping

COPY requirements.txt /script/requirements.txt
COPY find_min_mtu.py /script/find_min_mtu

RUN pip3 install --no-cache-dir -r requirements.txt
RUN chmod +x /script/find_min_mtu

ENTRYPOINT [ "/script/find_min_mtu" ]
