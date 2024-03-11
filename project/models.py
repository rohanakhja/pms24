from django.db import models
from user.models import User

# Create your models here.
techChoices = (
("Python","Python"),
("Java","Java"),
("C++","C++"),
("C#","C#"),
('Android','Android'),
)
class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=100,choices=techChoices)
    estimated_hours = models.PositiveIntegerField()
    startDate = models.DateField()
    endDate = models.DateField()
    
    class Meta:
        db_table = "project"
        
    def __str__(self):
        return self.name
    
class ProjectTeam(models.Model):
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    
    class Meta:
        db_table = "projectteam"
    
    def __str__(self):
        return self.user.username

statusChoices = (
    ("Not-started","Not-started"),
    ("In-progress","In-progress"),
    ("Testing","Testing"),
    ("Completed","Completed"),
)
    
class Status(models.Model):
    status_name = models.CharField(max_length=100,choices=statusChoices)
    
    class Meta:
        db_table = "status"
    
    def __str__(self):
        return self.status_name
        
class ProjectModule(models.Model):
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    module_name = models.CharField(max_length=100)
    description = models.TextField()
    estimated_hours = models.PositiveIntegerField()
    status = models.ForeignKey(Status,on_delete=models.CASCADE)
    startDate = models.DateField()
    
    class Meta:
        db_table = "project_module"
    
    def __str__(self):
        return self.module_name

priorityChoices = (
    ("High","High"),
    ("Medium","Medium"),
    ("Low","Low"),
)

class Task(models.Model):
    project_module = models.ForeignKey(ProjectModule,on_delete=models.CASCADE)
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    task_name = models.CharField(max_length=100)
    priority = models.CharField(max_length=100,choices=priorityChoices)
    description = models.TextField()
    status = models.ForeignKey(Status,on_delete=models.CASCADE)
    totalMinutes = models.PositiveIntegerField()
    is_assigned = models.BooleanField(default=False)
    
    class Meta:
        db_table="task"
        
    def __str__(self):
        return self.task_name
        
class UserTask(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    task = models.ForeignKey(Task,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated_at = models.DateTimeField(auto_now=True,null=True,blank=True)
    
    class Meta:
        db_table="user_task"
        
    def __str__(self):
        # return self.user.username
        return self.task.task_name + " -> " + self.user.username