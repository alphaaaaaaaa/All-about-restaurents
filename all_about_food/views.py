from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Restaurent,Dish
from .forms import SignUpForm
# Create your views here.

def loginView(request):
    login_form = AuthenticationForm()
    error = None
    if request.method == 'POST':
        login_form = AuthenticationForm(request=request, data=request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/all_about_restaurents/')
            else:
                error = "Invalid username or password."
        else:
            error = "Invalid username or password."  
    return render(request, 'login.html', {'login_form':login_form,'error':error})

def signupView(request):
    signup_form = SignUpForm()
    error = None
    if request.method == 'POST':
        signup_form = SignUpForm(request.POST)
        if signup_form.is_valid():
                signup_form.save()
                username = signup_form.cleaned_data.get('username')
                raw_password = signup_form.cleaned_data.get('password1')
                
                user = authenticate(username=username, password=raw_password)
                login(request, user)
                return redirect('/all_about_restaurents/')
            
    return render(request, 'signup.html', {'signup_form':signup_form})

def logoutView(request):
    logout(request)
    return redirect(loginView)

def homePageView(request):
    restaurents = Restaurent.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(restaurents, 3)
    try:
        restaurents = paginator.page(page)
    except PageNotAnInteger:
        restaurents = paginator.page(1)
    except EmptyPage:
        restaurents = paginator.page(paginator.num_pages)
    context = {
        'restaurents':restaurents,
        'active':'home',
    }
    return render(request,'homepage.html',context)
def categoryView(request,category):
    image = category + ".jpg"
    category = category.replace('-', ' ')
    restaurents = Restaurent.objects.filter(category=category)
    page = request.GET.get('page', 1)
    paginator = Paginator(restaurents, 3)
    try:
        restaurents = paginator.page(page)
    except PageNotAnInteger:
        restaurents = paginator.page(1)
    except EmptyPage:
        restaurents = paginator.page(paginator.num_pages)
    context = {
        'restaurents':restaurents,
        'image':image,
        'category':category,
        'active':category,
    }
    return render(request,'categories.html',context)
def restaurentView(request,id):
    restaurent = Restaurent.objects.get(id=id)
    print("test",restaurent.image)
    context = {
        'restaurent':restaurent
    }
    return render(request,'restaurent.html',context)

def searchView(request):
    q = request.GET.get("q")
    restaurents = Restaurent.objects.filter(address__icontains=q)
    
    dishes = Dish.objects.filter(name__icontains=q)
    
    context = {
        'restaurents':restaurents,
        'dishes':dishes,
        'search':True
    }
    return render(request,'homepage.html',context)

def aboutusView(request):
    return render(request,'about_us.html',{'active':'aboutus'})