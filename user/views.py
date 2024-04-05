from typing import Any
from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import User
from .forms import ManagerRegistrationForm,DeveloperRegistrationForm
#import settings.py file for mail sending
from django.conf import settings
#send_mail is built in function in django
from django.core.mail import send_mail
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import ListView
from project.models import Project,UserTask,Task,ProjectModule,Status,Bug
from django.shortcuts import get_object_or_404

# Create your views here.
class ManagerRegisterView(CreateView):
    model = User
    form_class = ManagerRegistrationForm
    template_name = "user/manager_register.html"
    success_url = "/user/login/"
    
    # def form_valid(self, form):
    #     email = form.cleaned_data.get('email')
    #     # print("email..",email)
    #     if sendMail(email):
    #         print("Email sent successfully")
    #         return super().form_valid(form)
    #     else:
    #         return super().form_valid(form)
    
    
class DeveloperRegisterView(CreateView):
    model = User
    form_class = DeveloperRegistrationForm
    template_name = "user/developer_register.html"
    success_url = "/user/login/"
    
def sendMail(to):
    subject = 'Welcome to PMS24'
    message = 'Project Management System Test mail'
    # recipientList = ['hkuchadiya24@gmail.com']
    recipientList = [to]
    EMAIL_FROM = settings.EMAIL_HOST_USER
    
    send_mail(subject, message, EMAIL_FROM, recipientList)
    
    # return HttpResponse("Email Sent..")
    return True

class UserLoginView(LoginView):
    template_name = "user/login.html"
    
    def get_redirect_url(self):
        if self.request.user.is_authenticated:
            if self.request.user.is_manager:
                return '/user/manager_dashboard/'
            else:
                return '/user/developer_dashboard/'
            
class UserLogoutView(LogoutView):
    def get_redirect_url(self):
        if not(self.request.user.is_authenticated):
            return '/user/login/'
            
class ManagerDashboardView(ListView):
    
    def get(self, request, *args, **kwargs):
        #logic to get all the projects
        total_task = Task.objects.count()
        total_projects = Project.objects.count()
        total_module = ProjectModule.objects.count()
        total_developer = User.objects.filter(is_developer = True).count()
        project = Project.objects.all() #select * from project
        # project = ProjectModule.objects.all()
        project_module = ProjectModule.objects.all()
        task = Task.objects.all()
        usertask = UserTask.objects.all()
        bug = Bug.objects.all()
      
        
        tasks_with_developers = []
        tasks = Task.objects.all()
        for task in tasks:
            user_task = UserTask.objects.filter(task=task).first()
            developer_name = user_task.user.username if user_task else None
           
            tasks_with_developers.append({'task': task, 'developer_name': developer_name  })
        # status = Status.objects.all()
        return render(request,"user/manager_dashboard.html",{
            'total_task': total_task,
            'total_developer':total_developer,
            'total_module': total_module,
            'total_projects': total_projects,
            'project':project,
            'project_module': project_module,
            'task': task,
            'usertask':usertask,
            'tasks_with_developers': tasks_with_developers,
            'bug': bug,
            # 'status': status,
            
        })
        
    
    template_name = "user/manager_dashboard.html"
    # context_object_name = "tasks_with_users"
    
class DeveloperDashboardView(ListView):
    
    def get(self, request, *args, **kwargs):
        user_tasks = UserTask.objects.filter(user=request.user)
        total_task = Task.objects.count()
        total_projects = Project.objects.count()
        total_module = ProjectModule.objects.count()
        total_developer = User.objects.filter(is_developer = True).count()
        project = Project.objects.all() #select * from project
        # project = ProjectModule.objects.all()
        project_module = ProjectModule.objects.all()
        task = Task.objects.all()#Filter task for the current developer
        bug = Bug.objects.all()
      
        return render(request,"user/developer_dashboard.html",{
            'user_tasks':user_tasks,
            'total_task': total_task,
            'total_developer':total_developer,
            'total_module': total_module,
            'total_projects': total_projects,
            'project':project,
            'project_module': project_module,
            'task': task,
            'bug': bug,
        })
    
    template_name = "user/developer_dashboard.html"
 


