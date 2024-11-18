from django.shortcuts import render
from django.http import HttpResponse
from .forms import taskForms

# Create your views here.
def index(request):
    return render(request,'index.html')
    #return HttpResponse("hi index")

#------------create taske------------------#
def create_task(request):
    form=taskForms()
    context={"form":form}
    return render(request,'create_task.html',context)
    #return HttpResponse("hi index")
