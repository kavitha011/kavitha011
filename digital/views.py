from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def homepage(request):
    return render(request,'index.html')

def student_form(request):
    if request.method =='POST':
        name=request.POST.get('name')
        rollno=request.POST.get('rollno')
        email=request.POST.get('email')
        student.objects.create(name=name,rollno=rollno,email=email)
        return redirect('student_form')
    students=student.objects.all()
    return render(request,'index.html',{'students':students})


def signup_view(request):
    if request.method == 'POST':
       username = request.POST.get('username')
       email = request.POST.get('email')
       password = request.POST.get('password')

       if User.objects.filter(username=username).exists():
          messages.error(request, "Username already exists.")
          return redirect('singup')

       user = User.objects.create_user(username=username, email=email, password=password)
       messages.success(request, "account created successfully.")
       return redirect('login')

    return render(request,'signup.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('student_form')    
        else:
            messages.error(request,"invalid credientials")
            return redirect('login')

    return render(request, 'login.html') 

def logout_view(request):
    logout(request)
    return redirect('login')       



def student_biodata(request):
    if request.method =='POST':
        age=request.POST.get('age')
        birth=request.POST.get('birth')
        gender=request.POST.get('gender')
        year=request.POST.get('year')
        department=request.POST.get('department')
        stream=request.POST.get('stream')
        mobile_no=request.POST.get('mobile_no')
        biodata.objects.create(age=age,birth=birth,gender=gender,year=year,department=department,stream=stream,mobile_no=mobile_no)
        return redirect('student_biodata')

    biodatas=biodata.objects.all()
    return render(request,'biodata.html',{'biodatas':biodatas})

def edit_biodata(request, pk):
    biodatas = get_object_or_404(biodata, pk=pk)

    if request.method == "POST":
        biodatas.age = request.POST.get("age")
        biodatas.department = request.POST.get("department")
        biodatas.stream = request.POST.get("stream")
        biodatas.save()
        return redirect("edit_biodata")

    return render(request,"edit.html", {
        "edit_biodata": biodatas,
        "biodatas": biodata.objects.all()
    })


def delete_biodata(request, pk):
    biodatas = get_object_or_404(biodata, pk=pk)
    biodatas.delete()
    return redirect("delete_biodata")
