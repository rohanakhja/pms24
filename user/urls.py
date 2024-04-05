from django.contrib import admin
from django.urls import path
from .views import ManagerRegisterView,DeveloperRegisterView,UserLoginView,ManagerDashboardView,DeveloperDashboardView,UserLogoutView
from . import views

urlpatterns = [
    path("manager_register/",ManagerRegisterView.as_view(),name="manager_register"),
    path("developer_register/",DeveloperRegisterView.as_view(),name="developer_register"),
    path("login/",UserLoginView.as_view(),name="login"),
    path("manager_dashboard/",ManagerDashboardView.as_view(),name="manager_dashboard"),
    path("developer_dashboard/",DeveloperDashboardView.as_view(),name="developer_dashboard"),
    path("logout/",UserLogoutView.as_view(),name="logout"),
    
    # path("manager-dashboard/", views.   , name='manager_dashboard'),
    
    # path("sendmail/",views.sendMail,name="sendmail"),
]