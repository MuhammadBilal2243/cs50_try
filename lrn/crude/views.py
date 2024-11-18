from django.shortcuts import render
from django.http import HttpResponse
from .forms import taskForms
from .models import tasks

# Create your views here.
def index(request):
    return render(request,'index.html')
    #return HttpResponse("hi index")

#------------create taske------------------#
def create_task(request):
    form =taskForms()
    if request.method == 'POST':
        form=taskForms(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("your task added to data sql3 db")
    context={"form":form}
    return render(request,'create_task.html',context)
    #return HttpResponse("hi index")
##__________-----------view_tasks_task---------------______________##
def view_tasks(request):
    task= tasks.objects.all()
    context={"tasks":task}
    return render(request, 'view_tasks.html',context)