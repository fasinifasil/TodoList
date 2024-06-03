from django.shortcuts import render,redirect

from ToDOApp.models import ToDOList
from .models import *
from .forms import *

# Create your views here.
def index(request): 
    List=ToDOList.objects.all()
    Listform=ToDoForm()
    if request.method=='POST':
        Listform=ToDoForm(request.POST)
        if Listform.is_valid():
            Listform.save()
        return redirect('/')

    CT={'key':List,'lock':Listform}
    return render(request,'indexpage.html',CT)



def update(request,k1):
    task =ToDOList.objects.get(id=k1)
    form=ToDoForm(instance=task)
    if request.method == 'POST':
        form = ToDoForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request,'update.html',context)


def delete(request,k1):
    item = ToDOList.objects.get(id=k1)
    if request.method == 'POST':
        item.delete()
        return redirect('/')
    context={'item':item}
    return render(request,'delete.html',context)