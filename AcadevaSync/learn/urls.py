from django.contrib import admin
from django.urls import path, include
from . import views,user_login
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('404/',views.PAGE_NOT_FOUND, name='404'),
    path('', views.HOME, name='home'),

    path('courses', views.SINGLE_COURSE, name='single_course'),
    path('courses/filter-data',views.filter_data,name="filter-data"), #course page filter
    path('course/<slug:slug>', views.COURSE_DETAILS, name='course_detail'),
    path('search',views.SEARCH_COURSE,name='search_course'),   # searchbar url
    path('contactus/', views.CONTACTUS, name='contactus'),
    path('aboutus/', views.ABOUTUS, name='aboutus'),

    path('accounts/register', user_login.REGISTER, name='register'), #register.html path
    path('accounts/', include('django.contrib.auth.urls')),       #login.html path   -login is builtin django module not necessary to build view of that -'accounts/login
    path('doLogin/', user_login.DO_LOGIN, name='doLogin'),
    path('accounts/profile/', user_login.PROFILE, name='profile'),     #profile update
    path('accounts/profile/update', user_login.PROFILE_UPDATE, name='profile_update'),

    path('checkout/<slug:slug>',views.CHECKOUT, name='checkout'),      #enroll free coure
    path('my-course/',views.MY_COURSE, name='my_course'),      #redirect after enroll free course
    path('verify_payment/',views.VERIFY_PAYMENT, name='verify_payment'),
    path('course/watch-course/<slug:slug>', views.WATCH_COURSE, name='watch_course'),    #watch course
    path('terms_of_services/',views.TERMS, name='terms_of_Service')

]+ static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
