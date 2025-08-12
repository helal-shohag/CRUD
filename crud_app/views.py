from django.shortcuts import render,redirect
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

# def show(request):
#     students = User.objects.all()
#     return render(request,'home.html',{'students':students})