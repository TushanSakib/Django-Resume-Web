from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import *
# Create your views here.

def home(request):
    resume = About.objects.all()
    education = Education.objects.all()
    interest = Interest.objects.all()
    reference = Reference.objects.all()
    project = Project.objects.all()
    return render(request,'home.html',{'resume':resume,'education':education,'interest':interest,'reference':reference,'project':project})



# Backend Sites

def about(request):
    if request.user.is_authenticated:
        about = About.objects.all()
        interest = Interest.objects.all()
        form = InterestForm(request.POST or None)
        if request.method == "POST":
            if form.is_valid():
                form.save()
                return redirect('about')

        return render(request,'about.html',{'about':about,'interest':interest,'form':form})

def update_interest(request,pk):
    if request.user.is_authenticated:
        interest = Interest.objects.get(id=pk)
        form = InterestForm(request.POST or None,instance=interest)
        if request.method == "POST":
            if form.is_valid():
                form.save()
                return redirect('about')
        return render(request,'update_interest.html',{'interest':interest,'form':form})

def delete_interest(request,pk):
    if request.user.is_authenticated:
        interest = Interest.objects.get(id=pk)
        interest.delete()
        return redirect('about')


def update_about(request,pk):
    if request.user.is_authenticated:
        about = About.objects.get(id=pk)
        form = AboutForm(request.POST or None,instance=about)
        if request.method == "POST":
            if form.is_valid():
                form.save()
                return redirect('about')
        return render(request,'update_about.html',{'about':about,'form':form})


def education(request):
    if request.user.is_authenticated:
        education = Education.objects.all()
        return render(request,'education.html',{'education':education})


def add_education(request):
    if request.user.is_authenticated:
        form = EducationForm(request.POST or None)
        if request.method == "POST":
            if form.is_valid():
                form.save()
                return redirect('education')
        return render(request,'add_education.html',{'education':education,'form':form})   


def update_education(request,pk):
    if request.user.is_authenticated:
        education = Education.objects.get(id=pk)
        form = EducationForm(request.POST or None,instance=education)
        if request.method == "POST":
            if form.is_valid():
                form.save()
                return redirect('education')
        return render(request,'update_education.html',{'education':education,'form':form})

def delete_education(request,pk):
    if request.user.is_authenticated:
        education = Education.objects.get(id=pk)
        education.delete()
        return redirect('education')


def reference(request):
    if request.user.is_authenticated:
        reference = Reference.objects.all()
        return render(request,'reference.html',{'reference':reference})


def add_reference(request):
    if request.user.is_authenticated:
        form = ReferenceForm(request.POST or None)
        if request.method == "POST":
            if form.is_valid():
                form.save()
                return redirect('reference')
        return render(request,'add_reference.html',{'form':form})


def update_reference(request,pk):
    if request.user.is_authenticated:
        reference = Reference.objects.get(id=pk)
        form = ReferenceForm(request.POST or None,instance=reference)
        if request.method == "POST":
            if form.is_valid():
                form.save()
                return redirect('reference')
        return render(request,'update_reference.html',{'reference':reference,'form':form})


def delete_reference(request,pk):
    if request.user.is_authenticated:
        reference= Reference.objects.get(id=pk)
        reference.delete()
        return redirect('reference')



def login_user(request):
    if request.method == "POST":
        username = request.POST['uname']
        password = request.POST['pass']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"You have been logged in...")
            return redirect('about')
        else:
            messages.success(request,"There was an error")
            return redirect('login')

    else:

        return render(request,'login.html',{})


def logout_user(request):
    logout(request)
    messages.success(request,"You have been logged out")
    return redirect('home')

def project(request):
    project = Project.objects.all()
    return render(request,'project_image.html',{'project':project})

def add_project(request):
    if request.user.is_authenticated:
        form = ProjectForm(request.POST or None)
        if request.method == "POST":
            if form.is_valid():
                form.save()
                return redirect('project')
        return render(request,'add_project.html',{'form':form})

def update_project(request,pk):
    if request.user.is_authenticated:
        project = Project.objects.get(id=pk)
        form = ProjectForm(request.POST or None,instance=project)
        if request.method == "POST":
            if form.is_valid():
                form.save()
                return redirect('project')
        return render(request,'update_project.html',{'project':project,'form':form})

def delete_project(request,pk):
    if request.user.is_authenticated:
        project= Project.objects.get(id=pk)
        project.delete()
        return redirect('project')



def project_images(request):
    images = Image.objects.all()
    return render(request,'images.html',{'images':images})



