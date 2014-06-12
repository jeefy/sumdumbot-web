#!/usr/bin/python
import os, sys

sys.path.insert(0, "/sumdumbot_web/app/")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "snaplink.settings")

from django.core.servers.fastcgi import runfastcgi

runfastcgi(method="threaded", daemonize="false")
