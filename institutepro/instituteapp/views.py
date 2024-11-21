from django.shortcuts import render,redirect
from .models import ContactData, CourseDetails
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def mainPage(request):
    return render(request, 'mainpage.html')

@login_required(login_url='login')
def home(request):
    return render(request, 'home.html')

@login_required(login_url='login')
def contact(request):
    if request.method == 'GET':
        return render(request, "contact.html")
    else:
        name1 = request.POST.get('name')
        mobile1 = request.POST.get('mobile')
        email1 = request.POST.get('email')
        address1 = request.POST.get('address')
        ContactData(
            name = name1,
            mobile = mobile1,
            email = email1,
            address = address1,
        ).save()
        return render(request, "contact.html")

@login_required(login_url='login')
def services(request):
    Data = CourseDetails.objects.all()
    return render(request, 'services.html',{'Data': Data})

@login_required(login_url='login')
def feedback(request):
    return render(request, 'feedback.html')

@login_required(login_url='login')
def gallery(request):
    return render(request, 'gallery.html')

def loginpage(request):
    if request.method == 'GET':
        return render(request,'login.html')
    else:
        username1 = request.POST['username']
        password1 = request.POST['password']
        user = authenticate(request, username=username1, password=password1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return render(request, 'login.html')
            
def logoutpage(request):
    logout(request)
    return redirect('mainpage')
