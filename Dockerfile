#docker run -d -v /home/planeswalker/container_data/sumdumbot_web/:/db "jeef/sumdumbot_web"

FROM ubuntu:14.04

RUN apt-get update && \
    apt-get -y upgrade && \
    apt-get -y install nginx python python-flup python-pip python-dev build-essential

ENV VIRTUAL_HOST otakushirts.com

EXPOSE 80

RUN service nginx stop

COPY ./sys/django.conf /etc/nginx/sites-enabled/django.conf
COPY ./app/ /sumdumbot_web/app/

WORKDIR /sumdumbot_web/app/

RUN pip install --upgrade pip && \
    pip install --allow-all-external -r requirements.txt 

CMD service nginx start && \
	python manage.py runfcgi host=127.0.0.1 port=8080 daemonize=false