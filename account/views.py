from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
import uuid
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.
@login_required(login_url='Login')
def home(request):
    return render(request,'home.html')


def Login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user_obj = User.objects.filter(username = username).first()
        if user_obj is None:
            messages.success(request, 'User not found.')
            return redirect('/login')
        
        
        profile_obj = Profile.objects.filter(user = user_obj ).first()

        if not profile_obj.verifiedid:
            messages.success(request, 'Profile is not verified check your mail.')
            return redirect('/login')

        myuser = authenticate(username = username , password = password)
        if myuser is None:
            messages.success(request, 'Wrong password.')
            return redirect('/login')
        
        login(request , myuser)
        return redirect('/')

    return render(request , 'login.html')

def signup_page(request):
    if request.method =='POST':
        username=request.POST['username']
        password=request.POST['password1']
        password1=request.POST['password2']
        token_id=str(uuid.uuid4())
        print(token_id)
        
        user1=User.objects.filter(username=username)
        if user1:
            messages.success(request,'Username already Exist')
            return redirect('/signup')
        
        if password!=password1:
            messages.success(request,'Password donot match')
            return redirect('/signup')
        
        my_user=User.objects.create_user(username,"",password)
        my_user.save()
        
        prof=Profile.objects.create(user=my_user,Auth_token=token_id)
        prof.save()
        email='aaryanshah615@gmail.com'
        send_mail_after_registration(email,token_id)
        messages.success(request,'Please verify your account Through Gmail')
        return redirect('/login')   
    
    return render(request,'signup.html')


def verify(request ,token):
    try:
        profile_obj = Profile.objects.filter(Auth_token =token).first()
    

        if profile_obj:
            if profile_obj.verifiedid:
                messages.success(request, 'Your account is already verified.')
                return redirect('/login')
            profile_obj.verifiedid= True
            profile_obj.save()
            messages.success(request, 'Your account has been verified.')
            return redirect('/login')
        else:
            return redirect('/')
    except Exception as e:
        print(e)
        return redirect('/')

    
def Logout(request):
    logout(request)
    return redirect('/')


def send_mail_after_registration(email , token):
    subject = 'Your accounts need to be verified'
    message =f'Hi click the link to verify your account http://127.0.0.1:8000/verify/{token}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message , email_from ,recipient_list )

    
