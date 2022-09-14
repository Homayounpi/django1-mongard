from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Todo
from django.contrib import messages
from .forms import TodoCreatForm,TodoupdateForm

# def say_hello(request):
#     return HttpResponse('say hello ...')

def say_hello(request):
    person = {'name': "homayoun",'number':'2'}
    return render(request,'hello.html',context=person)


def hellos(request):
    return HttpResponse('hellos user')


def home(request):
    all = Todo.objects.all()
    return render(request,'home.html',{'todos':all})


def detail(request,todo_id):
    todo=Todo.objects.get(id=todo_id)
    return render(request,'detail.html',{'todo':todo})


def delete(request,todo_id):
    Todo.objects.get(id=todo_id).delete()
    messages.success(request,'you mofagh shodid')
    return redirect('home')


def create(request):
    if request.method == 'POST' :
        form=TodoCreatForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            cd=form.cleaned_data
            Todo.objects.create(name=cd['titel'],body=cd['body'],crated=cd['created'])
            messages.success(request,'mofagh shodid ','success')
            return redirect('home')
    else:
        form=TodoCreatForm()
    return render(request,'create.html',{'form':form})

# 2022-07-23 13:15:13
def update(request,todo_id):
    todo=Todo.objects.get(id=todo_id)
    if request.method=='POST':
        form=TodoupdateForm(request.POST,instance=todo)
        if form.is_valid():
            form.save()
            messages.success(request,'update shod','success')
            return redirect('details',todo_id)


    else:
        form=TodoupdateForm(instance=todo)
    return render(request,'update.html',{'form':form})




