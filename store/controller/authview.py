from django.shortcuts import render,redirect
from django.contrib import messages
from store.forms import CustomUserForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.

# registration form #
def register_user(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Registered Successfully! Login to Continue.")
            return redirect('login')    #Replace'login' with the name of your URL pattern
    else:
        form = CustomUserForm()
    return render(request, 'store/auth/register.html', {'form':form})

# Login form #
def login_user(request):
    if request.user.is_authenticated:
        messages.warning(request,"You are already logged in!")
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request,"Logged in Successfully.")
                return redirect('home')
            else:
                messages.error(request,"Invalid Username or Password!")
                return redirect('login')
        
        return render(request, 'store/auth/login.html')

# Logout #
def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,"Logged Out Successfully.")
    return redirect('home')
