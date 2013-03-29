# Create your views here.
from link.models import Link

from django.shortcuts           import render_to_response
from django.template            import RequestContext
from django.contrib.auth        import authenticate, login, logout
from django.contrib.auth.models import User
from django.http                import HttpResponse
from django.utils               import simplejson
from django.db.models           import Count, Q
from django.core.paginator      import Paginator, EmptyPage, PageNotAnInteger
from django.db                  import connection

import datetime
import subprocess

def add(request):
	if request.GET.has_key('url') and request.GET.has_key('user') and request.GET.has_key('channel') and request.GET.has_key('title'):
		link = Link(url=request.GET['url'], user=request.GET['user'], channel=request.GET['channel'], title=request.GET['title'])
		link.save()
		#if request.GET['title'] == "Binary Data or File":
		#	p = subprocess.Popen(['wget', '-P', '/raid/archives/Incoming/sumdumbot/', request.GET['url']])
		return HttpResponse('OK')
	else:
		return HttpResponse('Error')

def index(request):
        return channel(request, "otakushirts")

def user(request, user):
	links = _page(Link.objects.filter(user=user).order_by('-timestamp'), request)

	tempvars = {'request':request, 'links':links, 'linkCount':len(links), 'channel':'otakushirts'}
	return render_to_response('index.html', tempvars)

def channel(request, channel):
        
	links = _page(Link.objects.filter(channel='#'+channel).order_by('-timestamp'), request)

	channels = []
	cursor = connection.cursor()
	cursor.execute("select channel from link_link group by channel;")        
	for n in cursor.fetchall():
		channels.append(n[0].strip('#'))

	tempvars = {'request':request, 'links':links, 'linkCount':len(links), 'channel':channel, 'channels':set(channels)}
	return render_to_response('index.html', tempvars)

def query(request, q):
	links = _page(Link.objects.filter(Q(title__icontains = q) | Q(url__icontains = q)).order_by('-timestamp'), request)
	
	tempvars = {'request':request, 'links':links, 'search':q, 'linkCount':len(links), 'channel':'otakushirts'}
	return render_to_response('index.html', tempvars)

def message(request):
	if request.method != 'GET' or not request.GET.has_key("message"):
		return HttpResponse("0")

	#import hashlib, urllib, simplejson
	#tmp     = request.POST["message"]
	#msg     = simplejson.loads(urllib.unquote(tmp))
	#message = msg['message']
	#key     = msg['key']
	#if message is not None and key is not None and key == hashlib.md5(message + 'sup ribs'):
	message = request.GET['message']
	f = open('/home/jeef/sumdumbot/messages.txt', 'w+')
	f.write(message)
	f.close()
	return HttpResponse("1")
	#else:
	#	return HttpResponse("0")
def _page(links, request):
	paginator = Paginator(links, 25) # Show 25 contacts per page

	page = request.GET.get('page')
	try:
		links = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		links = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
        	links = paginator.page(paginator.num_pages)
	return links
