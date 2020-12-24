from django.shortcuts import render,redirect
from .forms import CreateUserForm
from .models import Product
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.
def home_page(request):
    qs=Product.objects.order_by('-rating')[:30]
    context={'item_list':qs}
    return render (request,"home.html",context)

def signup_page(request):
    # form=CreateUserForm()
    if request.user.is_authenticated:
        return redirect("/home")
    else: 
        if request.method=="POST":
            form=CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user=form.cleaned_data.get('username')
                messages.success(request,"Account created for "+user)
                return redirect ('/home/login')
            else:
                print("Error in form")
                print(form.errors)
        else:
            form=CreateUserForm()
        context={'form':form}

        return render(request,"signup.html",context)

def login_page(request):
    if request.user.is_authenticated:
        return redirect("/home")
    else: 
        if request.method=='POST':
            username=request.POST.get('username')
            password=request.POST.get('password')
            user=authenticate(request,username=username,password=password)
            if(user is not None):
                login(request,user)
                return redirect ("/home")
            else :
                messages.info(request,"Username or password incorrect")
        return render(request,"login_page.html")

def logout_page(request):
    logout(request)
    return redirect("/home/login")
