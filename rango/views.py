from django.shortcuts import render

from django.http import HttpResponse

def index(request):

	#<a href="/rango/about/">About</a>

	#return HttpResponse("Rango says hey there partner")
	context_dict={'boldmessage':'Crunchy, creamy, cookie, candy!'}

	return render(request, 'rango/index.html', context=context_dict)


def about(request):

	#<a href='/rango/'>Index</a>
	#return HttpResponse("112223344555")

	return render(request,'rango/about.html')
