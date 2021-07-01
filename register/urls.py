
from django.urls import path, include
from register import views
urlpatterns = [

    path('home',views.home, name='home'),
    path('',views.login , name='login'),
    path('signup', views.signup, name='signup'),
    path('logout', views.log_out, name='logout'),
    path('verification/', include('verify_email.urls')),


]