from django.shortcuts import render ,  redirect
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
    context={"create_form":form}
    return render(request,'create_task.html',context)
    #return HttpResponse("hi index")
##__________-----------view_tasks_task---------------______________##
def view_tasks(request):
    task= tasks.objects.all()
    rev = list(reversed(task))
    context={"tasks": rev}

    return render(request, 'view_tasks.html',context)
##__________-----------update_tasks_task---------------______________##
def update_task(request,pk):
    task =tasks.objects.get(id=pk)
    form = taskForms(instance = task)
    if request.method =="POST":
        form = taskForms(request.POST,instance = task)
        if form.is_valid():
            form.save()
            return HttpResponse("task updated")
    context={"form":form}
    return render(request,'update_task.html',context)
###---------------delete_task----------------------###
def delete_task(request,pk):
    task =tasks.objects.get(id=pk)
    form = task.delete()
    return  redirect("view_tasks")




