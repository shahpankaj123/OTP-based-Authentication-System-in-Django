
from django.urls import path,include
from account import views

urlpatterns = [
    
    path('',views.home,name='home'),
    path('logout/',views.Logout,name='Logout'),
    path('login/',views.Login_page,name='Login'),
    path('signup/',views.signup_page,name='signup'),
    path('verify/<token>',views.verify),
]