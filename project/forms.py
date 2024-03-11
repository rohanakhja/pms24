from django import forms
from .models import Project,ProjectTeam,ProjectModule,Task,UserTask,Status
from user.models import User

class ProjectCreationForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
        widgets = {
            'startDate': forms.DateInput(attrs={'type': 'date'}),
            'endDate': forms.DateInput(attrs={'type': 'date'})
        }
        
class ProjectTeamCreationForm(forms.ModelForm):
    user = forms.ModelChoiceField(queryset=User.objects.filter(is_manager=True))
    class Meta:
        model = ProjectTeam
        fields = '__all__'
        
class ProjectStatusCreationForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = '__all__'
        
class ModuleCreationForm(forms.ModelForm):
    class Meta:
        model = ProjectModule
        fields = '__all__'
        widgets = {
            'startDate': forms.DateInput(attrs={'type': 'date'})
        }
        
class TaskCreationForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        
class TaskAssignForm(forms.ModelForm):
    user = forms.ModelChoiceField(queryset=User.objects.filter(is_developer=True))
    class Meta:
        model = UserTask
        fields = '__all__'