FROM ubuntu:18.04

ENV PYTHONUNBUFFERED=1

WORKDIR /workspace

COPY ./ ./

RUN apt update && apt -y upgrade && apt install -y \
  build-essential \
  libgl1-mesa-dev \
  python3 \
  python3-pip

RUN pip3 install --upgrade pip && pip3 install -r requirements.txt

ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8

EXPOSE 8501

CMD bash
