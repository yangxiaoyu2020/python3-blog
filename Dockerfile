FROM ubuntu:20.04
# base image

LABEL maintainer="frankysjtu@gmail.com"

ADD build_image/sources.list /etc/apt/sources.list

ADD build_image/get-pip.py ./


RUN apt-get update && \
    apt-get install -y vim supervisor python3.8 python3-distutils && \
    python3 get-pip.py

ADD build_image/pip.conf /root/.pip/pip.conf

WORKDIR /app

EXPOSE 9002

COPY requirements.txt /tmp/requirements.txt
COPY src ./src
COPY conf ./conf
COPY scripts ./scripts

RUN mkdir log_files&& \
    pip install -r /tmp/requirements.txt


RUN chmod +x ./scripts/start.sh

CMD ["./scripts/start.sh"]
# docker run -itd -p 9013:9002 test-blog:0.0.2
