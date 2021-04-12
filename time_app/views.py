from django.shortcuts import render,redirect,HttpResponse
from time import gmtime,strftime
from datetime import datetime

# Create your views here.
def index(request):
    context={
        "time":datetime.now()
        # "other_time":strftime("%Y-%m-%d %H:%M",gmtime())
    }
    return render(request,"index.html",context)
    
