from django.urls import reverse
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic.edit import CreateView,UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from user.models import User
from .models import Project,ProjectTeam,ProjectModule,Task,UserTask,Status
from .forms import ProjectCreationForm,ProjectTeamCreationForm,ModuleCreationForm,TaskCreationForm,TaskAssignForm,ProjectStatusCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic.edit import UpdateView

# Create your views here.
class ProjectCreationView(CreateView):
    model = Project
    form_class = ProjectCreationForm
    template_name = "project/create.html"
    success_url = "/project/list"

class ProjectListView(ListView):
    model = Project
    template_name = "project/list.html"
    context_object_name = "project"
    
class ProjectTeamCreateView(CreateView):
    model = ProjectTeam
    form_class = ProjectTeamCreationForm    
    template_name = 'project/create_team.html'
    success_url = '/project/list/'
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        project_id = self.request.GET.get('project_id')
        
        if project_id:
            project = get_object_or_404(Project, id=project_id)
            kwargs['initial']['project'] = project
        return kwargs

def project_team_view(request, id):
    project = ProjectTeam.objects.prefetch_related('user').filter(project_id=id)
    
    team_members = []
    for item in project:
        user = get_object_or_404(User, id=item.user_id)
        team_members.append({
            'username': user.username,
        })
        
    project = get_object_or_404(Project, id=id)
        
    return render(request, 'project/project_team.html', {'team_members': team_members, 'project' : project})

class ProjectUpdateview(UpdateView):
    model = Project
    form_class = ProjectCreationForm
    template_name = "project/update.html"
    success_url = "/project/list"
    
class ProjectDetailView(DetailView):
   model = Project
   context_object_name = "project"
   template_name = "project/detail.html"
        
def delete_project(request,id):
    project = Project.objects.get(id=id)
    
    project.delete()
    
    return HttpResponseRedirect("/project/list")

class ProjectTeamDetailView(DetailView):
   model = Project
   context_object_name = "project"
   template_name = "project/detail.html"
   
   
class ProjectStatusCreateView(CreateView):
    template_name = "project/status.html"
    model = Status
    success_url = "/project/list"
    form_class = ProjectStatusCreationForm
    

def taskStatusUpdateView(request,id):
    task = Task.objects.get(id=id)
    
    if task.status.status_name == "Not-started":
        task.status_id = 2
    elif task.status.status_name == "In-progress":
        task.status_id = 3
    elif task.status.status_name == "Testing":
        task.status_id = 4
        
    task.save()
    
    return redirect(reverse('developer_dashboard'))

class ModuleCreationView(CreateView):
    model = ProjectModule
    form_class = ModuleCreationForm
    template_name = "project/create_module.html"
    success_url = "/project/list_module"
    
class ModuleListView(ListView):
    model = ProjectModule
    template_name = "project/list_module.html"
    context_object_name = "module"
    
class ModuleUpdateview(UpdateView):
    model = ProjectModule
    form_class = ModuleCreationForm
    template_name = "project/update_module.html"
    success_url = "/project/list_module"
    
class ModuleDetailView(DetailView):
   model = ProjectModule
   context_object_name = "module"
   template_name = "project/detail_module.html"
        
def delete_module(request,id):
    module = ProjectModule.objects.get(id=id)
    
    module.delete()
    
    return HttpResponseRedirect("/project/list_module")

class TaskCreationView(CreateView):
    model = Task
    form_class = TaskCreationForm
    template_name = "project/create_task.html"
    success_url = "/project/list_task"

class TaskListView(ListView):
    model = Task
    template_name = "project/list_task.html"
    context_object_name = "task"
    
class TaskUpdateview(UpdateView):
    model = Task
    form_class = TaskCreationForm
    template_name = "project/update_task.html"
    success_url = "/project/list_task"
    
class TaskDetailView(DetailView):
   model = Task
   context_object_name = "task"
   template_name = "project/detail_task.html"
        
def delete_task(request,id):
    task = Task.objects.get(id=id)
    
    task.delete()
    
    return HttpResponseRedirect("/project/list_task")

class TaskAssignView(CreateView):
    model = UserTask
    form_class = TaskAssignForm
    template_name = "project/task_assign.html"
    success_url = "/project/list"