#docker.io run -d -v /home/planeswalker/container_data/sumdumbot_web/:/db "jeef/sumdumbot_web"

FROM ubuntu:12.04

RUN apt-get update
RUN apt-get -y upgrade
RUN apt-get -y install nginx git python python-django python-flup 
    
RUN git clone https://github.com/jeefy/sumdumbot-web.git /sumdumbot_web/
RUN mv /sumdumbot_web/sys/django.conf /etc/nginx/sites-enabled/django.conf

RUN service nginx stop

ENV VIRTUAL_HOST otakushirts.com

EXPOSE 80

CMD cd /sumdumbot_web/ && \
	git pull && \
	service nginx start && \
	cd app && \
	python manage.py runfcgi host=127.0.0.1 port=8080 daemonize=false