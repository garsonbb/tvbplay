from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound
from .models import link

from .collecter.collect import tvb

# Create your views here.

def index(request):
    return render(request,'index.html')

def page404(request):
    return HttpResponse('<h1>Nothing here</h1>\n<h2>(＃°Д°)</h2><h3>404</h3>')

def page500(request):
    return HttpResponse('<h1>!!!</h1>\n<h2>(＃°Д°)</h2><h3>500</h3>')


def aihuijia(request):
    context = {'items':link.objects.all()}
    return render(request,'base.html',context)

def player(request,num):
    src = link.objects.get(linkTitle__contains=num)
    print(src.linkUrl)
    context = {'src': src.linkUrl}
    return render(request,"baseplayer.html",context)

def collect(request):
    link.objects.all().delete()
    foo = tvb('http://www.hktvyb.com/vod/detail/id/947.html')
    foo.collect()
    for i in range(len(foo.resultTitles)):
        l = link()
        l.linkTitle = foo.resultTitles[i]
        l.linkUrl   = foo.resultUrls[i]
        l.save()

    return HttpResponse("done!")