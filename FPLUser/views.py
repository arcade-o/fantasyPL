from django.shortcuts import render,redirect
from .models import FPLUser
from django.views import View
from django.contrib.auth.models import auth
from django.contrib.auth import get_user_model
from django.contrib import messages
from rest_framework import generics
from .serializers import FPLUser_serializer

User=get_user_model()

# Create your views here.

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        if password1 == password2:
            user = FPLUser.objects.create_user(email=email,password=password1,username=username)
            return redirect('login')
        return render(request,'signup.html')
    return render(request,'signup.html')

def login(request):
    if request.method == "POST":
        identifier = request.POST.get('identifier')
        password = request.POST.get('password')
        if FPLUser.objects.filter(username=identifier):
            temp_user = FPLUser.objects.get(username=identifier)
            user = auth.authenticate(request,email=temp_user.email,password=password)
            if user is not None:
                auth.login(request,user)
                return redirect('/')
            messages.info(request,'Invalid password')
            return redirect('login')
        if FPLUser.objects.filter(email=identifier):
            user = auth.authenticate(request,email = identifier,password=password)
            if user is not None:
                auth.login(request,user)
                return redirect('/')
            messages.info(request,'Invalid password')
            return redirect('login')
        messages.info(request,'Username/email does not exist')
        return redirect('login')
    return render(request,'login.html')
    
def logout(request):
    auth.logout(request)
    return redirect('/')

class FPLUserAPI(generics.ListAPIView,generics.UpdateAPIView,generics.DestroyAPIView):
    serializer_class = FPLUser_serializer

    def get_queryset(self):
        if "id" in self.kwargs:
            return FPLUser.objects.get(id=self.kwargs['id']).order_by('-points').values()
        return FPLUser.objects.all().order_by('-points').values()
    
    def get_object(self):
        return FPLUser.objects.get(id=self.kwargs['id'])
    
    def update(request,self,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    
    def delete(request,self,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)
    

    


