
from django.contrib import admin
from django.urls import path,include
from courses.views import my_courses,home,coursePage,SignupView,LoginView,signout,checkout,verifyPayment
from django.conf import settings
from django.conf.urls.static import static
from codewithnaveen.settings import MEDIA_ROOT,MEDIA_URL 
urlpatterns = [
    
 path('',home, name='home'),
 path('logout',signout, name='logout'),
 path('my-courses',my_courses, name='my-courses'),
 path('signup', SignupView.as_view() , name='signup'),
 path('login',LoginView.as_view(), name='login'),
 path('course/<str:slug>',coursePage, name='coursepage'),
 path('check-out/<str:slug>',checkout, name='check-out'),
 path('verify_payment',verifyPayment, name='verify_payment'),
 
]  
urlpatterns+= static(MEDIA_URL, document_root=MEDIA_ROOT)


urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)