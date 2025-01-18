from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    goal = models.IntegerField()
    image = models.URLField()
    is_open = models.BooleanField()
    date_created = models.DateTimeField(auto_now_add = True)
    owner = models.ForeignKey(
        get_user_model(),  # which model is this a fk to?
        on_delete=models.CASCADE,  # what should we do if the User is deleted?
        related_name='owned_projects'  # what is it called when we go backwards
    )

# adding an update model that links to the project model to view project updates 
# class Update(models.Model):
#     project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='updates')
#     title = models.CharField(max_length=200)
#     content = models.TextField()
#     date_created = models.DateTimeField(auto_now_add = True)

    # Get project id=1 from the database
    # project = Project.objects.get(pk=1)
    # project.owner_id (1)
    # project.title (Test Project)
    # owner = CustomUser.objects.get(project.owner_id)
    # project.owner <= user model instead of the id number
    #
    # user = CustomUser.objects.get(pk=1)
    # user.owned_projects <= backwards link via the foreign key

class Pledge(models.Model):
    amount =  models.IntegerField()
    comment = models.CharField(max_length=200)
    anonymous = models.BooleanField()
    project = models.ForeignKey(
        'Project',
        on_delete=models.CASCADE,
        related_name='pledges'
    )
    supporter = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='pledges', 
        null=True,
        blank=True
    )