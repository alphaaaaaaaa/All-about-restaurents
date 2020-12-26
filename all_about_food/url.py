from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('aboutus',views.aboutusView,name='aboutus'),
    path('search',views.searchView,name='search'),
    path('login',views.loginView,name='login'),
    path('signup',views.signupView,name='signup'),
    path('logout',views.logoutView,name='logout'),
    path('', views.homePageView,name='homepage'),
    path('restaurent/<int:id>',views.restaurentView,name='restaurent'),
    path('<str:category>',views.categoryView,name='category'),

]