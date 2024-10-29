from django.shortcuts import render, redirect

from django.http import HttpResponse

from myApp.models import *

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def homePage(req):

    return render(req, 'home.html')

def registerPage(req):

    if req.method == 'POST':
        
        username = req.POST.get('username')
        email = req.POST.get('email')
        profile_pic = req.FILES.get('profile_picture')
        user_type = req.POST.get('user_type')
        password = req.POST.get('password')
        confirm_password = req.POST.get('confirm_password')

        if password == confirm_password:

            user = Custom_User.objects.create_user(
                username = username,
                email = email,
                profile_pic = profile_pic,
                user_type = user_type,
                password = confirm_password 
            )

            if user_type == 'viewer':
                RecipeViewerModel.objects.create(user=user)
            
            elif user_type == 'creator':
                RecipeCreatorModel.objects.create(user=user)

            return redirect('loginPage')

    return render(req, 'register.html')

def loginPage(req):

    username = req.POST.get('username')
    password = req.POST.get('password')

    user = authenticate(req, username=username, password=password)

    if user is not None:
        login(req,user)
        return redirect('homePage')
    
    
    return render(req, 'login.html')

def logoutPage(req):
    logout(req)

    return redirect('loginPage')

@login_required
def profilePage(req):

    return render(req, 'profile.html')

@login_required
def editProfile(req):

    current_user = req.user

    if req.method == 'POST':
        current_user.username = req.POST.get('username')
        current_user.email = req.POST.get('email')
        current_user.user_type = req.POST.get('user_type')
        
        if req.FILES.get('profile_picture'):
            current_user.profile_pic = req.FILES.get('profile_picture')
        
        current_user.save()
        return redirect('profilePage')

    return render(req,'edit_profile.html')