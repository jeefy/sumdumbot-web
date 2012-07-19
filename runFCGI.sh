#!/bin/bash

# Replace these three settings.
PROJDIR="/home/jeef/srv/http/otakushirts/snaplink/"
PIDFILE="$PROJDIR/mysite.pid"
SOCKET="$PROJDIR/mysite.sock"

cd $PROJDIR
if [ -f $PIDFILE ]; then
    kill `cat -- $PIDFILE`
    rm -f -- $PIDFILE
fi

exec /usr/bin/env - \
  PYTHONPATH="../python:.." \
  python manage.py runfcgi pidfile=$PIDFILE method=prefork maxspare=2 daemonize=false

#  python manage.py runfcgi socket=$SOCKET pidfile=$PIDFILE umask=000
