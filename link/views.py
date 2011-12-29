# Create your views here.
from link.models import Link

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.cache import cache
from django.http import HttpResponse
from django.utils import simplejson
from django.db.models import Count

import datetime

def index(request, urldate=None):
	today = datetime.date.today()
	next_day = None
	
	if urldate is None:
		links = Link.objects.filter(timestamp__year=today.year, timestamp__month=today.month, timestamp__day=today.day).order_by('-timestamp')
		previous_day = today - datetime.timedelta(days=1)
	else:
		tmp = urldate.split('-')
		print tmp
		curdate = datetime.date(int(tmp[0]), int(tmp[1]), int(tmp[2]))
		links = Link.objects.filter(timestamp__year=curdate.year, timestamp__month=curdate.month, timestamp__day=curdate.day).order_by('-timestamp')
		
		previous_day = curdate - datetime.timedelta(days=1)
		print curdate
		print today
		if curdate != today:
			next_day = curdate + datetime.timedelta(days=1)

	tempvars = {'request':request, 'links':links, 'previous_day':previous_day, 'next_day':next_day}
	return render_to_response('index.html', tempvars)

def user(request, user):
	links = Link.objects.filter(user=user).order_by('-timestamp')

	tempvars = {'request':request, 'links':links}
	return render_to_response('index.html', tempvars)
