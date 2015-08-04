#docker run -d -v /home/planeswalker/container_data/sumdumbot_web/:/db "jeef/sumdumbot_web"

FROM ubuntu:14.04

RUN apt-get update && \
    apt-get -y upgrade && \
    apt-get -y install nginx python python-django python-flup

ENV VIRTUAL_HOST otakushirts.com

EXPOSE 80

RUN service nginx stop

COPY ./sys/django.conf /etc/nginx/sites-enabled/django.conf

CMD service nginx start && \
    cd /sumdumbot_web/app && \
	python manage.py runfcgi host=127.0.0.1 port=8080 daemonize=false