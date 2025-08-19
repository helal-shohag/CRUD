from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import UserForm
from .models import User
# Create your views here.
def home(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
           name = form.cleaned_data['name']
           email = form.cleaned_data['email']       
           password = form.cleaned_data['password'] 
           user = User(name=name, email=email, password=password)
           user.save()
         
    else:
        form =UserForm()
    return render(request, 'home.html',{'form': form,'students': User.objects.all()})

def delete(request,id):
    user = User.objects.get(pk= id)
    user.delete()
    return HttpResponseRedirect('/')

def update(request,id):
    if request.method == 'POST':
        user = User.objects.get(pk = id)
        form = UserForm(request.POST,instance=user)
        if form.is_valid():
            form.save()

    else:
        user = User.objects.get(pk=id)
        form = UserForm(instance=user)
    return render(request,'update.html',{'form':form})
